#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
consistency_checker.py

Evaluates consistency across multiple GPT responses. This can be used to 
identify contradictions or drifting narratives, especially in deception studies.

Usage:
  from consistency_checker import ConsistencyChecker

  cc = ConsistencyChecker()
  conversation_responses = ["I like apples.", "I do not like apples."]
  consistency_report = cc.check_consistency(conversation_responses)
  print(consistency_report)
"""

class ConsistencyChecker:
    def __init__(self):
        pass

    def check_consistency(self, responses):
        """
        Basic demonstration: checks for straightforward repeated contradiction 
        in a list of strings.

        :param responses: list of str
        :return: dict with a consistency flag or contradiction details
        """
        # Very naive example: look for direct negation
        contradictory = False
        if len(responses) >= 2:
            for i in range(len(responses) - 1):
                if " not " in responses[i].lower() and " not " not in responses[i+1].lower():
                    contradictory = True

        return {
            "contradiction_found": contradictory,
            "evaluated_count": len(responses)
        }
