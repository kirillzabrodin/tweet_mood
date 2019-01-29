from django.test import TestCase
import unittest
from unittest import mock
from unittest.mock import patch, Mock, ANY
from ..tweeterpy import Tweeterpy

class TweeterpyUnitTests(TestCase):
    def Strips_hashtags_links_and_ats(self):
        tweets = Tweeterpy()
        result = tweets.format_output("RT #hello @testing https://www.test-this.com")
        assert result == "   "

    # def test_send_for_analysis_calls_get_result(self):
    #     mock_response_object = Mock()
    #     mock_response_object.get_result = Mock(return_value={})
    #     mock_tone_analyzer = Mock()
    #     mock_tone_analyzer.analyze = Mock(return_value=mock_response_object)
    #     watson = Watson(mock_tone_analyzer)
    #     watson.send_for_analysis('test text', 'test')
    #     mock_response_object.get_result.assert_called_once()
