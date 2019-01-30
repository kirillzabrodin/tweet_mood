import json
from watson_developer_cloud import NaturalLanguageUnderstandingV1
from watson_developer_cloud.natural_language_understanding_v1 import Features, EntitiesOptions, KeywordsOptions, EmotionOptions
import os

class Watson:

    NLU_DATE = '2018-11-16'
    NLU_URL = 'https://gateway-lon.watsonplatform.net/natural-language-understanding/api'
    NLU_API_KEY = os.environ.get('WATSON_TEXT_ANALYZER')

    def __init__(self, text_analyzer = NaturalLanguageUnderstandingV1(
        version=NLU_DATE,
        iam_apikey=NLU_API_KEY,
        url=NLU_URL
    )):
        self.text_analyzer = text_analyzer

    def send_for_analysis(self, tweets, word):
        return self.text_analyzer.analyze(
            text=tweets,
            features=Features(
                keywords=KeywordsOptions(
                    emotion=True,limit=2
                ),
                emotion=EmotionOptions(
                    targets=[word],
                    document=True
                )
            )
        ).get_result()
