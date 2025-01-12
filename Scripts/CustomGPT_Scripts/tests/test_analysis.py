#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
test_analysis.py

Basic tests for verifying analysis modules.
Run with pytest or another test framework.
"""

import pytest
from ..analysis.response_analyzer import ResponseAnalyzer
from ..analysis.sentiment_tracker import SentimentTracker

def test_response_analyzer():
    ra = ResponseAnalyzer()
    analysis = ra.analyze_response("This is a fact with evidence.")
    assert analysis["truth_markers"] is True

def test_sentiment_tracker():
    st = SentimentTracker()
    result = st.get_sentiment("I love testing code!")
    assert "label" in result
    assert "confidence" in result
