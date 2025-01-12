#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
response_logger.py

Logs GPT interactions (prompts and responses) in a structured format for 
later analysis, auditing, or debugging.

Usage:
  from response_logger import ResponseLogger

  logger = ResponseLogger("experiment_log.txt")
  logger.log_interaction("User Prompt", "GPT Response")
"""

import datetime

class ResponseLogger:
    def __init__(self, log_file="gpt_responses.log"):
        self.log_file = log_file

    def log_interaction(self, prompt, response):
        """
        Writes a timestamped record of the prompt and GPT response to the log file.
        """
        timestamp = datetime.datetime.now().isoformat()
        record = f"{timestamp}\nPROMPT: {prompt}\nRESPONSE: {response}\n\n"
        with open(self.log_file, "a", encoding="utf-8") as f:
            f.write(record)
