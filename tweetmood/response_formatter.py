class ResponseFormatter:

    def __init__(self):
        self.formatted_response_dict = {
          "joy" : 0,
          "anger" : 0,
          "sadness" : 0,
          "fear" : 0,
          "disgust" : 0,
         }

    def process(self, response):
        print(response)
        for tone in response['emotion']['targets']:
            for key in tone['emotion']:
                self.formatted_response_dict[key] = round(tone['emotion'][key] * 100)
