#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
rate_limiter.py

Handles API rate limits and queuing of requests if necessary. Useful 
for controlling throughput and preventing API lockouts.

Usage:
  from rate_limiter import RateLimiter

  rl = RateLimiter(max_requests_per_min=60)
  rl.wait_for_slot()
  # Proceed with API call
"""

import time

class RateLimiter:
    def __init__(self, max_requests_per_min=60):
        self.max_requests_per_min = max_requests_per_min
        self.interval = 60 / max_requests_per_min
        self.last_request_time = 0

    def wait_for_slot(self):
        """
        Ensures requests are spaced out to avoid exceeding rate limits.
        """
        current_time = time.time()
        elapsed = current_time - self.last_request_time
        if elapsed < self.interval:
            time.sleep(self.interval - elapsed)
        self.last_request_time = time.time()
