from textblob import TextBlob


class Holmes:

    def __init__(self, textblob=TextBlob):
        self.textblob = textblob

    def holmes_analysis(self, text):
        analysis = self.textblob(text)
        score = analysis.sentiment.polarity
        if score >= 0.5:
            return "very positive"
        elif 0.1 <= score < 0.5:
            return "positive"
        elif -0.1 < score < 0.1:
            return "neutral"
        elif -0.5 < score <= -0.1:
            return "negative"
        else:
            return "very negative"
