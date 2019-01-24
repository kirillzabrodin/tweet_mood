import json
from watson_developer_cloud import ToneAnalyzerV3
import os

class Watson:

    DATE = '2017-09-21'
    URL = 'https://gateway-lon.watsonplatform.net/tone-analyzer/api/v3/tone?version=2017-09-21&sentences=false'
    API_KEY = os.environ.get('WATSON_TONE_ANALYZER')

    def __init__(self, tone_analyzer = ToneAnalyzerV3(
        version=DATE,
        iam_apikey=API_KEY,
        url=URL
    )):
        self.tone_analyzer = tone_analyzer

    def send_for_analysis(self, text):
        return self.tone_analyzer.tone(
            { 'text': text },
            'application/json'
        ).get_result()
