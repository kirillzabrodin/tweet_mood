class ResponseFormatter:

    def __init__(self):
        self.formatted_response_dict = {
          "Joy" : 0,
          "Anger" : 0,
          "Sadness" : 0,
          "Analytical" : 0,
          "Fear" : 0,
          "Disgust" : 0,
          "Confident" : 0,
          "Tentative" : 0
         }

    def process(self, response):
        for tone in response['document_tone']['tones']:
          self.formatted_response_dict[tone['tone_name']] = int((tone['score']) * 100)
