class ResponseFormatter:

    def __init__(self):
        self.formatted_response_dict = {}

    def process(self, response):
        for tone in response['emotion']['targets']:
            for key in tone['emotion']:
                self.formatted_response_dict[key] = (tone['emotion'][key] * 100)
