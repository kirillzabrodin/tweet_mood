import json
from watson_developer_cloud import ToneAnalyzerV3
import os

api_key = os.environ.get('WATSON_TONE_ANALYZER')

class ToneAnalyzer:

    def __init__(self, tone_analyzer = ToneAnalyzerV3):
        self.tone_analyzer = tone_analyzer(
            version='2017-09-21',
            iam_apikey=api_key,
            url= 'https://gateway-lon.watsonplatform.net/tone-analyzer/api/v3/tone?version=2017-09-21&sentences=false'
        )

    def send_for_analysis(self, text):
        tone_analysis = self.tone_analyzer.tone(
            { 'text': text },
            'application/json',
        ).get_result()
        return json.dumps(tone_analysis)
