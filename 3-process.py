import os.path
assert os.path.isfile("aclImdb/alldata-id.txt"), "alldata-id.txt unavailable"

import gensim
from gensim.models.doc2vec import TaggedDocument
from collections import namedtuple

SentimentDocument = namedtuple('SentimentDocument', 'words tags split sentiment')

alldocs = []  # will hold all docs in original order
with open('aclImdb/alldata-id.txt', encoding='utf-8') as alldata:
    for line_no, line in enumerate(alldata):
        tokens = gensim.utils.to_unicode(line).split()
        words = tokens[1:]
        tags = [line_no] # `tags = [tokens[0]]` would also work at extra memory cost
        split = ['train','test','extra','extra'][line_no//25000]  # 25k train, 25k test, 25k extra
        sentiment = [1.0, 0.0, 1.0, 0.0, None, None, None, None][line_no//12500] # [12.5K pos, 12.5K neg]*2 then unknown
        alldocs.append(SentimentDocument(words, tags, split, sentiment))

train_docs = [doc for doc in alldocs if doc.split == 'train']
test_docs = [doc for doc in alldocs if doc.split == 'test']
doc_list = alldocs[:]  # for reshuffling per pass

print('%d docs: %d train-sentiment, %d test-sentiment' % (len(doc_list), len(train_docs), len(test_docs)))

# distinct file?

from gensim.models import Doc2Vec
import gensim.models.doc2vec
from collections import OrderedDict
import multiprocessing

cores = multiprocessing.cpu_count()
assert gensim.models.doc2vec.FAST_VERSION > -1, "this will be painfully slow otherwise"

simple_models = [
    # PV-DM w/concatenation - window=5 (both sides) approximates paper's 10-word total window size
    Doc2Vec(dm=1, dm_concat=1, size=100, window=5, negative=5, hs=0, min_count=2, workers=cores),

    # PV-DBOW
    Doc2Vec(dm=0, size=100, negative=5, hs=0, min_count=2, workers=cores),

    # PV-DBOW w/ word training
    Doc2Vec(dm=0, dbow_words=1, size=100, negative=5, hs=0, min_count=2, workers=cores),

    # PV-DM w/average
    Doc2Vec(dm=1, dm_mean=1, size=100, window=10, negative=5, hs=0, min_count=2, workers=cores),
]

# speed setup by sharing results of 1st model's vocabulary scan
simple_models[0].build_vocab(alldocs)  # PV-DM/concat requires one special NULL word so it serves as template
print(simple_models[0])
for model in simple_models[1:]:
    model.reset_from(simple_models[0])
    print(model)

models_by_name = OrderedDict((str(model), model) for model in simple_models)

# This is how you concatenate two models -- presumably for other vectors as well
#from gensim.test.test_doc2vec import ConcatenatedDoc2Vec
#models_by_name['dbow+dmm'] = ConcatenatedDoc2Vec([simple_models[1], simple_models[2]])
#models_by_name['dbow+dmc'] = ConcatenatedDoc2Vec([simple_models[1], simple_models[0]])
# skipped because these cannot be saved with .save()
# TODO: concatenated vector option for similarity, analogies, and doc_similarity

# Helper methods for determining error rates
import numpy as np
import statsmodels.api as sm
from random import sample

# for timing
from contextlib import contextmanager
from timeit import default_timer
import time

@contextmanager
def elapsed_timer():
    start = default_timer()
    elapser = lambda: default_timer() - start
    yield lambda: elapser()
    end = default_timer()
    elapser = lambda: end-start

def logistic_predictor_from_data(train_targets, train_regressors):
    logit = sm.Logit(train_targets, train_regressors)
    predictor = logit.fit(disp=0)
    #print(predictor.summary())
    return predictor

def error_rate_for_model(test_model, train_set, test_set, infer=False, infer_steps=3, infer_alpha=0.1, infer_subsample=0.1):
    """Report error rate on test_doc sentiments, using supplied model and train_docs"""

    train_targets, train_regressors = zip(*[(doc.sentiment, test_model.docvecs[doc.tags[0]]) for doc in train_set])
    train_regressors = sm.add_constant(train_regressors)
    predictor = logistic_predictor_from_data(train_targets, train_regressors)

    test_data = test_set
    if infer:
        if infer_subsample < 1.0:
            test_data = sample(test_data, int(infer_subsample * len(test_data)))
        test_regressors = [test_model.infer_vector(doc.words, steps=infer_steps, alpha=infer_alpha) for doc in test_data]
    else:
        test_regressors = [test_model.docvecs[doc.tags[0]] for doc in test_docs]
    test_regressors = sm.add_constant(test_regressors)

    # predict & evaluate
    test_predictions = predictor.predict(test_regressors)
    corrects = sum(np.rint(test_predictions) == [doc.sentiment for doc in test_data])
    errors = len(test_predictions) - corrects
    error_rate = float(errors) / len(test_predictions)
    return (error_rate, errors, len(test_predictions), predictor)

## Bulk training

from collections import defaultdict
best_error = defaultdict(lambda :1.0)  # to selectively-print only best errors achieved

from random import shuffle
import datetime

alpha, min_alpha, passes = (0.025, 0.001, 20)
alpha_delta = (alpha - min_alpha) / passes

print("START %s" % datetime.datetime.now())

for epoch in range(passes):
    shuffle(doc_list)  # shuffling gets best results

    for name, train_model in models_by_name.items():
        # train
        duration = 'na'
        train_model.alpha, train_model.min_alpha = alpha, alpha
        with elapsed_timer() as elapsed:
            train_model.train(doc_list)
            duration = '%.1f' % elapsed()

        # evaluate
        eval_duration = ''
        with elapsed_timer() as eval_elapsed:
            err, err_count, test_count, predictor = error_rate_for_model(train_model, train_docs, test_docs)
        eval_duration = '%.1f' % eval_elapsed()
        best_indicator = ' '
        if err <= best_error[name]:
            best_error[name] = err
            best_indicator = '*'
        print("%s%f : %i passes : %s %ss %ss" % (best_indicator, err, epoch + 1, name, duration, eval_duration))

        if ((epoch + 1) % 5) == 0 or epoch == 0:
            eval_duration = ''
            with elapsed_timer() as eval_elapsed:
                infer_err, err_count, test_count, predictor = error_rate_for_model(train_model, train_docs, test_docs, infer=True)
            eval_duration = '%.1f' % eval_elapsed()
            best_indicator = ' '
            if infer_err < best_error[name + '_inferred']:
                best_error[name + '_inferred'] = infer_err
                best_indicator = '*'
            print("%s%f : %i passes : %s %ss %ss" % (best_indicator, infer_err, epoch + 1, name + '_inferred', duration, eval_duration))

    print('completed pass %i at alpha %f' % (epoch + 1, alpha))
    alpha -= alpha_delta

print("END %s" % str(datetime.datetime.now()))

# Debugging save
print("Now saving models...")

# The model name is not suitable for a filename
def extract_model_filename(raw_name, dir_name="models/"):
    filename = raw_name.replace("/","+").replace("Doc2Vec(","").split(",")[0]
    return dir_name + filename + ".model"

# Apparently, you cannot save the ConcatenatedDoc2Vec objects
# (Investigate - maybe it's surplus, but I thought it was trained separately?)
for name, train_model in models_by_name.items():
    if name.startswith("Doc2Vec"):
        filename = extract_model_filename(name)
        train_model.save(filename)
        print("Saved", filename)

print("Have saved models to directory 'models'.")
