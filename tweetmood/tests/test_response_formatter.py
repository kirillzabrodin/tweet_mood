from django.test import TestCase
import pytest
from ..response_formatter import ResponseFormatter

class TestResponseFormatter(TestCase):
    def test_processes_response_and_turns_into_dictionary(self):
        response = {'emotion': {'targets': [{'text': 'death', 'emotion': {'sadness': 0.372566, 'joy': 0.116822, 'fear': 0.084264, 'disgust': 0.540895, 'anger': 0.16676}}]}}
        desired_result = {'joy': 12, 'anger': 17, 'sadness': 37, 'fear': 8, 'disgust': 54}
        response_formatter = ResponseFormatter()
        response_formatter.process(response)
        assert desired_result == response_formatter.formatted_response_dict
