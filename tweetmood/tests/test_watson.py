from django.test import TestCase
import unittest
from doubles import ObjectDouble, allow, expect
from unittest import mock
from unittest.mock import patch
from watson_developer_cloud import ToneAnalyzerV3
from ..watson import Watson
from unittest.mock import MagicMock

class WatsonUnitTests(unittest.TestCase):
    def test_send_for_analysis(self):
        tone_analyzer = MagicMock()
        watson = Watson(tone_analyzer)
        watson.send_for_analysis('text')
        tone_analyzer.tone.assert_called_with({ 'text': 'text' },
        'application/json')

#  1
# expect subject to respond to send_for_analysis

#  2
# allow tone_analyzer double to receive get_result()
# expect the tone_analyzer double to receive tone()

# 3
# allow tone_analyzer double to receive tone().and_return('text analysis')
# expect the tone_analyzer to receive get_result()
