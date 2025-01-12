#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
response_analyzer.py

Analyzes GPT responses for linguistic or contextual cues related to truth, 
deception, or other experiment-specific markers. Integrates NLP or 
statistical methods as needed.

Usage:
  from response_analyzer import ResponseAnalyzer

  analyzer = ResponseAnalyzer()
  analysis_result = analyzer.analyze_response("Sample GPT response text...")
  print(analysis_result)
"""

import re

class ResponseAnalyzer:
    def __init__(self):
        # Simple sets or dictionaries for demonstration
        self.deception_keywords = {"lie", "fake", "fabrication", "misleading"}
        self.truth_keywords = {"fact", "data", "evidence", "truth"}

    def analyze_response(self, response_text):
        """
        Returns a dictionary with basic analysis results (truth vs deception markers, etc.).

        :param response_text: str, the GPT response to analyze.
        :return: dict, analysis results including found markers.
        """
        lower_text = response_text.lower()
        found_deception = any(word in lower_text for word in self.deception_keywords)
        found_truth = any(word in lower_text for word in self.truth_keywords)

        return {
            "length": len(response_text),
            "deception_markers": found_deception,
            "truth_markers": found_truth
        }
