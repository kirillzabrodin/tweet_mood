from django.test import TestCase
import mock
import pytest
from pytest_mock import mocker
from ..watson import ToneAnalyzer

#  1
# expect subject to respond to send_for_analysis

#  2
# allow tone_analyzer double to receive get_result()
# expect the tone_analyzer double to receive tone()

# 3
# allow tone_analyzer double to receive tone().and_return('text analysis')
# expect the tone_analyzer to receive get_result()
