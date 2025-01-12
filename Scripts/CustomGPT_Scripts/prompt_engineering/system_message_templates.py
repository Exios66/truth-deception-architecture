#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
system_message_templates.py

Holds template text for different GPT persona system messages, 
including scenario-specific prompts (truth or deception, etc.).
"""

class SystemMessageTemplates:
    def __init__(self):
        # Example placeholders for scenario templates
        self.scenario_templates = {
            "truth_scenario_1": "System Persona: Honest Investigator\nInstructions: Provide factual, verifiable information.",
            "deception_scenario_1": "System Persona: Deceptive Actor\nInstructions: Provide misleading or false information subtly."
        }

    def get_scenario_template(self, scenario_key):
        """
        Retrieves a pre-defined scenario template.
        """
        return self.scenario_templates.get(
            scenario_key, 
            "System Persona: Default\nInstructions: Provide a generic response."
        )
