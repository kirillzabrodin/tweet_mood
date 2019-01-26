# from textblob import TextBlob
# from textblob.classifiers import NaiveBayesClassifier
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
