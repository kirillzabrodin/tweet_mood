from textblob import TextBlob


class Holmes:

    def holmes_analysis(self, text):
        analysis = TextBlob(text)
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
