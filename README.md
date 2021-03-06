# IMDB analysis with Doc2Vec

This repository is my adaptation of [this very helpful tutorial](https://github.com/RaRe-Technologies/gensim/blob/develop/docs/notebooks/doc2vec-IMDB.ipynb). Because I wanted to adapt this to my own uses later, I decided to break it down into a series of scripts.

*My setup:* I used Python 3.4, installed through Anaconda. The
additional packages needed are `gensim` and `statsmodels`.

### Processing Data and Training the Models

The model training  should take a couple of hours on a reasonably
fast machine, many more on a slow laptop. Once the models have been
trained, however, they are saved so that the analysis scripts can be
run very quickly.

1. Run the `1-prep.py` script. This downloads the IMDB sentiment database file and does some file setup.

2. Run the `2-folders.py` script. This processes the files in the `aclImdb` folder so that they are in a proper form for Doc2Vec.

3. Run the `3-process.py` script. This is a time-consuming step, but at the end, you should have some models saved to the `models/` folder.

## Exploring the Models

These are the models trained by the scripts above. All four of them contain trained document vectors. Three of them also contain usefully trained word vectors. (The plain "dbow" model lacks trained word vectors.)

* `dm+m.model`

* `dm+c.model`

* `dbow.model` - This version of the "distributed bag of words" trains only the document vectors, not the word vectors. The authors of the reference code said the performance was no worse for sentiment analysis. But it generates junk on the word-analysis tools (as it should, because the word vectors are not trained after being randomly initialized).

* `dbow+w.model` - This version *does* train the word vectors, along with the document vectors.

These models can be loaded into a python shell using the normal `gensim` syntax for loading a Doc2Vec model. I have also written the scripts below to explore the word and document vectors.

### Word Vectors

* `similarity.py` - This script lets you pick a word from the corpus and see which other words are deemed closest by Word2Vec.

  If you invoke the script without arguments, a word is chosen at random for you.

  Alternatively, you can suggest one or more words as arguments and (if each word is in the database a sufficient number of times to yield interesting results), you will see what other words in the corpus are deemed similar to each word you have listed.

* `analogies.py` - This script assesses the accuracy of the models against a set of analogies published by Google with the original Word2Vec implementation.

  Keep in mind the IMDB data set is very small and that it is focused on a narrow problem domain. Even so, the system has learned a fair number of relative meanings.

### Document Similarity

* `doc_similarity.py` - This draws one document (movie review) at random and then displays (1) the three most similar items in the dataset, (2) one item that is perfectly at the median (neither similar nor dissimilar), and (3) the single least-similar review.

  You can adjust which model is invoked by changing that variable at the top of the script file.

**Skipped:** Although the IMDB dataset is usually used to evaluate sentiment analysis, I am less interested in that question so I did not include that in my scripts.
