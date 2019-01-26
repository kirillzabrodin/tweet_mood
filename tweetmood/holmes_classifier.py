from textblob import TextBlob
from textblob.classifiers import NaiveBayesClassifier
from nltk.corpus import movie_reviews
import random

reviews = [(list(movie_reviews.words(fileid)), category)
              for category in movie_reviews.categories()
              for fileid in movie_reviews.fileids(category)]

# random.shuffle(reviews)
# train, test = reviews[0:1800], reviews[1800:2000]

# print('train on %d instances, test on %d instances' % (len(train), len(test)))

# classifier = NaiveBayesClassifier(train)
# print('accuracy:', classifier.accuracy(test))
# print(classifier.classify("I love the world"))
