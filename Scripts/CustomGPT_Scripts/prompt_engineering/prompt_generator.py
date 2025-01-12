#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
prompt_generator.py

Dynamically creates prompts for various experimental conditions in the 
truth and deception study. Integrates with templates, user input, and 
context to produce a well-formatted prompt suitable for GPT.

Usage:
  from prompt_generator import PromptGenerator

  pg = PromptGenerator(model="gpt-4")
  prompt = pg.generate_prompt("deception_scenario_1", additional_context="User's prior statement.")
  print(prompt)
"""

import os
from .system_message_templates import SystemMessageTemplates
from ..utils.api_wrapper import ApiWrapper


class PromptGenerator:
    def __init__(self, model="gpt-4"):
        self.model = model
        self.templates = SystemMessageTemplates()
        self.api_wrapper = ApiWrapper()

    def generate_prompt(self, scenario_key, additional_context=""):
        """
        Generate a GPT prompt by combining scenario template with optional context.
        
        :param scenario_key: str, used to fetch the relevant template from SystemMessageTemplates.
        :param additional_context: str, appended or integrated into the template.
        :return: str, final combined prompt.
        """
        template = self.templates.get_scenario_template(scenario_key)
        final_prompt = f"{template}\n\nAdditional Context:\n{additional_context}"
        return final_prompt
