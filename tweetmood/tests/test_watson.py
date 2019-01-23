from django.test import TestCase
import unittest
from unittest import mock
from unittest.mock import patch
from watson_developer_cloud import ToneAnalyzerV3
from ..watson import Watson

class WatsonUnitTests(TestCase):
    def test_send_for_analysis(self):
        with mock.patch('watson_developer_cloud.ToneAnalyzerV3') as mock_analyzer:
            watson = Watson(mock_analyzer)
            watson.send_for_analysis('test text')
            mock_analyzer.tone.assert_called_once_with({ 'text': 'test text' },
            'application/json')
