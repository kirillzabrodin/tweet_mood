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
        emotion_response = response['emotion']['targets'][0]['emotion']
        for key in emotion_response:
            self.formatted_response_dict[key] = round(emotion_response[key] * 100)
