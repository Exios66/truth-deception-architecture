#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
performance_metrics.py

Tracks performance metrics like response times, token usage, and 
operational overhead. Useful for optimization and monitoring.

Usage:
  from performance_metrics import PerformanceMetrics

  pm = PerformanceMetrics()
  pm.start_timer()
  # ... API call
  pm.end_timer()
  print(pm.get_elapsed_time())
"""

import time

class PerformanceMetrics:
    def __init__(self):
        self.start_time = 0
        self.end_time = 0
        self.last_elapsed = 0

    def start_timer(self):
        self.start_time = time.perf_counter()

    def end_timer(self):
        self.end_time = time.perf_counter()
        self.last_elapsed = self.end_time - self.start_time

    def get_elapsed_time(self):
        return self.last_elapsed
