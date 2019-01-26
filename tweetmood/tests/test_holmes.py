from django.test import TestCase
import unittest
from unittest import mock
from unittest.mock import patch, Mock
from ..holmes import Holmes


class HolmesUnitTests(TestCase):
    def test_very_positive(self):
        mock_textblob = Mock()
        mock_textblob.sentiment.polarity = 0.75
        holmes = Holmes()
        assert holmes.holmes_analysis('love') == 'very positive'

    def test_positive(self):
        mock_textblob = Mock()
        mock_textblob.sentiment.polarity = 0.45
        holmes = Holmes()
        assert holmes.holmes_analysis('fine') == 'positive'

    def test_neutral(self):
        mock_textblob = Mock()
        mock_textblob.sentiment.polarity = 0.05
        holmes = Holmes()
        assert holmes.holmes_analysis('test') == 'neutral'

    def test_negative(self):
        mock_textblob = Mock()
        mock_textblob.sentiment.polarity = -0.45
        holmes = Holmes()
        assert holmes.holmes_analysis('average') == 'negative'

    def test_very_negative(self):
        mock_textblob = Mock()
        mock_textblob.sentiment.polarity = -0.75
        holmes = Holmes()
        assert holmes.holmes_analysis('hate') == 'very negative'
