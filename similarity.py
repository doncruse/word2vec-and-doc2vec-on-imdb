# word similarity lists

# parameters
minimum_n = 20      # exclude infrequent words
model_name = "dm+c.model" # "dm+c.model"
                          # "dm+m.model"
                          # avoid "dbow" because it has not been trained
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

# load up the model
model = Doc2Vec.load(model_path + model_name)

# load the corresponding vocabulary list

# accept list of words as arguments - if none, draw one word at random
word_list = sys.argv
word_list.remove(sys.argv[0]) # get rid of script name

randomized = False
if len(word_list) == 0:
    randomized = True
    while True:
        word = random.choice(model.index2word)
        if model.vocab[word].count >= minimum_n:
            word_list.append(word)
            break

for word in word_list:
    if word not in model.vocab:
        print(word, "is not present in this corpus.")
        print()

    elif model.vocab[word].count < minimum_n:
        print(word, "appears fewer than", minimum_n, "times in this corpus.")
        print()

    else:
        similar_words = [str(model.most_similar(word, topn=20)).replace('), ','),<br>\n')]

        if randomized:
            print("WORD DRAWN AT RANDOM...", word)
            print()

        print(word, "is similar to:")
        print(similar_words)
        print()

print("To repeat, invoke similarity.py with words as arguments")
