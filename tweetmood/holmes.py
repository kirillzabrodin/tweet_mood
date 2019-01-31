from textblob.classifiers import NaiveBayesClassifier

def feelings(number):
    if number >= 75:
        return "supremely positive"
    elif 55 <= number < 75:
        return "generally positive"
    elif 45 <= number < 55:
        return "ambivalent"
    elif 25 <= number < 45:
        return "rather negative"
    else:
        return "overwhelmingly negative"

with open('tweetmood/holmes_data/reformatted_small_train.csv', 'r') as train:
    trained_classifier = NaiveBayesClassifier(train)

class Holmes:

    def __init__(self, classifier=trained_classifier):
        self.classifier = classifier

    def holmes_classify(self, text):
        result = self.classifier.prob_classify(text)
        pos = int(round(result.prob('4'), 2) * 100)
        neg = int(round(result.prob('0'), 2) * 100)
        pwid = pos / 2
        nwid = neg / 2
        feeling = feelings(pos)
        return {"pos": pos, "neg": neg, "pwid": pwid, "nwid": nwid, "feeling": feeling}
