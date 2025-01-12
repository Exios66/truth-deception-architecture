#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
config_manager.py

Manages configuration settings, including environment variable loading 
and fallback to defaults. 
"""

import os
from dotenv import load_dotenv

class ConfigManager:
    def __init__(self, env_file=".env"):
        load_dotenv(env_file)

    def get(self, key, default=None):
        """
        Retrieve configuration value by key from environment variables.
        """
        return os.getenv(key, default)