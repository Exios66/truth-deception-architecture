#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
test_prompts.py

Simple tests for verifying prompt creation logic in PromptGenerator.
Run with pytest or another test framework.

Usage:
  pytest test_prompts.py
"""

import pytest
from ..prompt_engineering.prompt_generator import PromptGenerator

def test_generate_prompt():
    pg = PromptGenerator(model="gpt-4")
    prompt = pg.generate_prompt("truth_scenario_1", "Additional user context.")
    assert isinstance(prompt, str)
    assert "Honest Investigator" in prompt