from django.test import TestCase
import unittest
from unittest import mock
from unittest.mock import patch, Mock
from ..holmes_classifier import HolmesClassifier


class HolmesClassifierUnitTests(TestCase):

    def test_classify(self):
        mock_prob = Mock()
        mock_prob.prob = Mock(return_value=0.50)
        mock_NBC = Mock()
        mock_NBC.prob_classify = Mock(return_value=mock_prob)
        holmes = HolmesClassifier(mock_NBC)
        assert holmes.holmes_classify('love') == {"pos": 50, "neg": 50}
