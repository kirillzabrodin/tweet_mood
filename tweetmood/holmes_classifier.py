from textblob import TextBlob
from textblob.classifiers import NaiveBayesClassifier
# from nltk.corpus import movie_reviews
# import random


# The following formats the movie_reviews dataset into a list:
# reviews = [(list(movie_reviews.words(fileid)), category)
             # for category in movie_reviews.categories()
             # for fileid in movie_reviews.fileids(category)]

# The following shuffles the list then assigns it to training and testing sets
# random.shuffle(reviews)
# train, test = reviews[0:1800], reviews[1800:2000]

# This is just nice for the shell:
# print('train on %d instances, test on %d instances' % (len(train), len(test)))

# This creates a new classifier and trains it on the randomised training set:
# classifier = NaiveBayesClassifier(train)

# More that is nice for the shell:
# print('accuracy:', classifier.accuracy(test))

# This runs text through the classifier and returns pos or neg:
# print(classifier.classify("I love the world"))
train = [
     ('I love this sandwich.', 'pos'),
     ('this is an amazing place!', 'pos'),
     ('I feel very good about these beers.', 'pos'),
     ('this is my best work.', 'pos'),
     ("what an awesome view", 'pos'),
     ('I do not like this restaurant', 'neg'),
     ('I am tired of this stuff.', 'neg'),
     ("I can't deal with this", 'neg'),
     ('he is my sworn enemy!', 'neg'),
     ('my boss is horrible.', 'neg'),
     ('I am neutral', 'neu'),
     ('this is average', 'neu'),
     ('i am here', 'neu')
 ]
test = [
     ('the beer was good.', 'pos'),
     ('I do not enjoy my job', 'neg'),
     ("I ain't feeling dandy today.", 'neg'),
     ("I feel amazing!", 'pos'),
     ('Gary is a friend of mine.', 'pos'),
     ("I can't believe I'm doing this.", 'neg'),
     ('today is monday', 'neu')
 ]

cl = NaiveBayesClassifier(train)
print(cl.classify("I love the world"))
prob_dist = (cl.prob_classify("I love the world"))
print(prob_dist.max())
print(round(prob_dist.prob("pos"), 2))
print(round(prob_dist.prob("neg"), 2))
print(round(prob_dist.prob("neu"), 2))
