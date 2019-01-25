from django.test import TestCase
import pytest
from ..response_formatter import ResponseFormatter

class TestResponseFormatter(TestCase):
    def test_processes_response_and_turns_into_dictionary(self):
        response = {'document_tone': {'tones': [{'score': 0.835076, 'tone_id': 'joy', 'tone_name': 'Joy'}, {'score': 0.762356, 'tone_id': 'analytical', 'tone_name': 'Analytical'}]}}
        desired_result = {'Joy': 83, 'Anger': 0, 'Sadness': 0, 'Analytical': 76, 'Fear': 0, 'Disgust': 0, 'Confident': 0, 'Tentative': 0}
        response_formatter = ResponseFormatter()
        response_formatter.process(response)
        assert desired_result == response_formatter.formatted_response_dict
