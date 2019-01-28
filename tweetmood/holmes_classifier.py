from textblob import TextBlob
from textblob.classifiers import NaiveBayesClassifier

with open('tweetmood/formatted_test.csv', 'r') as train:
    trained_classifier = NaiveBayesClassifier(train)

class HolmesClassifier:

    def __init__(self, classifier = trained_classifier):
        self.classifier = classifier

    def holmes_classify(self, text):
        result = self.classifier.prob_classify(text)
        pos = int(round(result.prob('4'), 2) * 100)
        neg = int(round(result.prob('0'), 2) * 100)
        return {"pos": pos, "neg": neg}
