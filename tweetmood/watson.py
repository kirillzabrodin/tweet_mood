import json
from watson_developer_cloud import ToneAnalyzerV3
from watson_developer_cloud import NaturalLanguageUnderstandingV1
from watson_developer_cloud.natural_language_understanding_v1 import Features, EntitiesOptions, KeywordsOptions, EmotionOptions
import os

class Watson:

    DATE = '2017-09-21'
    URL = 'https://gateway-lon.watsonplatform.net/tone-analyzer/api/v3/tone?version=2017-09-21&sentences=false'
    API_KEY = os.environ.get('WATSON_TONE_ANALYZER')

    NLU_DATE = '2018-11-16'
    NLU_URL = 'https://gateway-lon.watsonplatform.net/natural-language-understanding/api'
    NLU_API_KEY = os.environ.get('WATSON_TEXT_ANALYZER')

    def __init__(self, tone_analyzer = ToneAnalyzerV3(
        version=DATE,
        iam_apikey=API_KEY,
        url=URL
    ), text_analyzer = NaturalLanguageUnderstandingV1(
        version=NLU_DATE,
        iam_apikey=NLU_API_KEY,
        url=NLU_URL
    )):
        self.tone_analyzer = tone_analyzer
        self.text_analyzer = text_analyzer

    def send_for_analysis(self, text):
        response = self.tone_analyzer.tone(
            { 'text': text },
            'application/json',
        )
        return response.get_result()

    def send_for_full_analysis(self, tweets, word):
        response = self.text_analyzer.analyze(
            text=tweets,
            features=Features(
                entities=EntitiesOptions(),
                keywords=KeywordsOptions(),
                emotion=EmotionOptions(
                    targets=[word],
                    document=False
                )
            )
        )
        print(tweets)
        print(response)
        return response.get_result()
