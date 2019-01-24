
class WatsonFormatter:
    def formatter(self, analysed_text):
        for tone in analysed_text["document_tone"]["tones"]:
            (tone['tone_name'], tone['score'])
