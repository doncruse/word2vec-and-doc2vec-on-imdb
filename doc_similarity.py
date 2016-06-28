# examine document similarity
#
# for a particular model, see which documents are most and least like
# an example drawn at random

model_name = "dbow+w.model" # "dm+c.model"
                            # "dm+m.model"
                            # "dbow+w.model" (has trained word vectors)
                            # "dbow.model" (documents trained; words not)
model_path = "models/"
data_path = "aclImdb/"

# setting up the environment
import locale
locale.setlocale(locale.LC_ALL, 'C')
import gensim
from gensim.models.doc2vec import TaggedDocument
from collections import namedtuple
from gensim.models import Doc2Vec
import gensim.models.doc2vec
from collections import OrderedDict
import multiprocessing
import numpy as np
import statsmodels.api as sm
import random
from random import shuffle
import sys

# optional
# from gensim.tests.test_doc2vec import ConcatenatedDoc2Vec

# confirm local files exist
import os.path
assert os.path.isfile(data_path + "alldata-id.txt"), "alldata-id.txt is unavailable"
assert os.path.isfile(model_path + model_name), model_name + " is unavailable"

print("The program will choose one document at random, and then identify the",
      "three most similar, one least similar, and a the most perfectly 'median'",
      "document -- using the trained model", model_name)
print()

# accept list of words as arguments - if none, draw one word at random
#word_list = sys.argv
#word_list.remove(sys.argv[0]) # get rid of script name

# load up the model
model = Doc2Vec.load(model_path + model_name)

# load all_docs
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
# I don't think the train/test matters for this purpose, but it's in the reference code

# adapted from https://github.com/RaRe-Technologies/gensim/blob/develop/docs/notebooks/doc2vec-IMDB.ipynb
doc_id = np.random.randint(model.docvecs.count)  # pick random doc, re-run cell for more examples
sims = model.docvecs.most_similar(doc_id, topn=model.docvecs.count)  # get *all* similar documents
print(u'TARGET (%d): «%s»\n' % (doc_id, ' '.join(alldocs[doc_id].words)))
print(u'SIMILAR/DISSIMILAR DOCS PER MODEL %s:\n' % model)
for label, index in [('MOST', 0), ('SECOND MOST', 1), ('THIRD MOST', 2), ('MEDIAN', len(sims)//2), ('LEAST', len(sims) - 1)]:
    print(u'%s %s: «%s»\n' % (label, sims[index], ' '.join(alldocs[sims[index][0]].words)))
