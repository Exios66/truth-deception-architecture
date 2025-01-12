#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
token_manager.py

Manages API tokens, usage, and costs. Tracks token consumption to stay within budget 
and prevent unexpected charges. Potentially integrates real-time usage monitoring.

Usage:
  from token_manager import TokenManager

  tm = TokenManager()
  tm.record_token_usage(1500)
  print(tm.get_total_tokens_used())
"""

class TokenManager:
    def __init__(self):
        self.total_tokens_used = 0
        self.token_limit = 1_000_000  # For demonstration

    def record_token_usage(self, count):
        """
        Add token usage to the running total and return updated total usage.
        """
        self.total_tokens_used += count
        return self.total_tokens_used

    def get_total_tokens_used(self):
        return self.total_tokens_used

    def under_limit(self):
        """
        Check if total tokens used is under the specified limit.
        """
        return self.total_tokens_used <= self.token_limit
