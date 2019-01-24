from django.test import TestCase
import unittest
from unittest import mock
from unittest.mock import patch, Mock
from watson_developer_cloud import ToneAnalyzerV3
from ..watson import Watson

class WatsonUnitTests(TestCase):
    def test_send_for_analysis(self):
        mock_response_object = Mock()
        mock_response_object.get_result = Mock(return_value={})
        mock_tone_analyzer = Mock()
        mock_tone_analyzer.tone = Mock(return_value=mock_response_object)
        watson = Watson(mock_tone_analyzer)
        watson.send_for_analysis('test text')
        mock_tone_analyzer.tone.assert_called_once_with({ 'text': 'test text' },
        'application/json')
        mock_response_object.get_result.assert_called_once()
