class WatsonFormatter:
    def format(self, format_text):
        for tone in format_text['document_tone']['tones']:
            (tone['tone_name'], tone['score'])
