import json
from watson_developer_cloud import ToneAnalyzerV3
from watson_developer_cloud import NaturalLanguageUnderstandingV1
from watson_developer_cloud.natural_language_understanding_v1 import Features, CategoriesOptions
import os

class Watson:

    DATE = '2017-09-21'
    URL = 'https://gateway-lon.watsonplatform.net/tone-analyzer/api/v3/tone?version=2017-09-21&sentences=false'
    API_KEY = os.environ.get('WATSON_TONE_ANALYZER')

    def __init__(self, tone_analyzer = ToneAnalyzerV3(
        version=DATE,
        iam_apikey=API_KEY,
        url=URL
    ), text_analyzer = NaturalLanguageUnderstandingV1(
        version=DATE,
        iam_apikey=API_KEY,
        url=URL
    )):
        self.tone_analyzer = tone_analyzer
        self.text_analyzer = text_analyzer

    def send_for_analysis(self, text):
        response = self.tone_analyzer.tone(
            { 'text': text },
            'application/json',
        )
        print(text)
        print(response)
        return response.get_result()

    def send_for_second_analysis(self, text):
        response = self.text_analyzer.analyze(
            { 'text': text },
            'application/json',
            features=Features(
                concepts=ConceptsOptions(limit=3),
                categories=CategoriesOptions(limit=3))
        )
        print(text)
        print(response)
        return response.get_result()
