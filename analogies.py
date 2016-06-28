# test the models for how they perform on analogies
#
# dbow is not trained (in this implementation) so it should perform terribly
model_names = ["dm+m.model", "dm+c.model", "dbow.model", "dbow+w.model"]
model_path = "models/"
data_path = "aclImdb/"
top_n_words = 2500

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

analogy_filename = "analogies/questions-words.txt"
assert os.path.isfile(analogy_filename), analogy_filename + " is unavailable"
print("Now processing... (please be patient)")

# note: this takes many minutes
# adapted from https://github.com/RaRe-Technologies/gensim/blob/develop/docs/notebooks/doc2vec-IMDB.ipynb
#
# I retrieved "questions-words.txt" from this archived Google repo:
# https://code.google.com/archive/p/word2vec/source/default/source
# and placed it in the "analogies/" directory.

# shifting to a hash so I can fold in concatenated models later
models_by_name = {}
for model_name in model_names:
    assert os.path.isfile(model_path + model_name), model_name + " is unavailable"
    models_by_name[model_name] = Doc2Vec.load(model_path + model_name)

#from gensim.test.test_doc2vec import ConcatenatedDoc2Vec
#models_by_name['dbow+dmm'] = ConcatenatedDoc2Vec([models_by_name["dbow.model"], models_by_name["dm+m.model"]])
#models_by_name['dbow+dmc'] = ConcatenatedDoc2Vec([models_by_name["dbow.model"], models_by_name["dm+c.model"]])
# apparently... this model has no attribute "accuracy", so this doesn't work

for model_name, model in models_by_name.items():
    print()
    print("Testing", model_name)
    sections = model.accuracy(analogy_filename)
    correct, incorrect = len(sections[-1]['correct']), len(sections[-1]['incorrect'])
    print("Results of testing", model_name, "against file", analogy_filename)
    print('%s: %0.2f%% correct (%d of %d)' % (model, float(correct*100)/(correct+incorrect), correct, correct+incorrect))
    sections = model.accuracy(analogy_filename, top_n_words)
    correct, incorrect = len(sections[-1]['correct']), len(sections[-1]['incorrect'])
    print("... restricted to top", top_n_words,"words")
    print('%s: %0.2f%% correct (%d of %d)' % (model, float(correct*100)/(correct+incorrect), correct, correct+incorrect))
