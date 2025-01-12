#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
api_wrapper.py

Provides a higher-level interface around the OpenAI API calls. 
Uses environment variables for API keys and model parameters.

Usage:
  from api_wrapper import ApiWrapper

  api = ApiWrapper()
  response = api.send_prompt("Hello, GPT!")
  print(response)
"""

import os
import openai
from .config_manager import ConfigManager
from ..experimental.rate_limiter import RateLimiter
from ..experimental.token_manager import TokenManager

class ApiWrapper:
    def __init__(self):
        self.config = ConfigManager()
        self.rate_limiter = RateLimiter()
        self.token_manager = TokenManager()
        openai.api_key = self.config.get("OPENAI_API_KEY")
        self.model = self.config.get("DEFAULT_MODEL", "gpt-4")
        self.temperature = float(self.config.get("TEMPERATURE", "0.7"))
        self.max_tokens = int(self.config.get("MAX_TOKENS", "2000"))

    def send_prompt(self, prompt, **kwargs):
        """
        Sends a prompt to the OpenAI API using default or custom parameters.
        """
        self.rate_limiter.wait_for_slot()
        try:
            response = openai.ChatCompletion.create(
                model=kwargs.get("model", self.model),
                messages=[{"role": "user", "content": prompt}],
                max_tokens=kwargs.get("max_tokens", self.max_tokens),
                temperature=kwargs.get("temperature", self.temperature),
                n=1
            )
            usage = response["usage"]["total_tokens"]
            self.token_manager.record_token_usage(usage)

            return response["choices"][0]["message"]["content"]
        except Exception as e:
            # Basic error handling; more robust logic can be delegated to error_handler
            print(f"OpenAI API Error: {e}")
            return None