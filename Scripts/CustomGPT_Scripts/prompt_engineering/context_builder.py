#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
context_builder.py

Maintains contextual information across conversations. Could be extended 
to handle advanced conversation state, user metadata, or partial GPT responses.

Usage:
  from context_builder import ContextBuilder

  cb = ContextBuilder()
  cb.add_message("user", "Hello, how are you?")
  cb.add_message("assistant", "I'm fine, thank you!")
  conversation_history = cb.get_conversation()
"""

class ContextBuilder:
    def __init__(self):
        self.history = []

    def add_message(self, role, content):
        """
        Adds a new message to the conversation history.
        
        :param role: str, either 'user' or 'assistant'.
        :param content: str, the text content of the message.
        """
        self.history.append({
            "role": role,
            "content": content
        })

    def get_conversation(self):
        """
        Returns the full conversation history for additional processing or prompt creation.
        """
        return self.history

    def clear_history(self):
        """
        Clears the entire conversation history.
        """
        self.history = []
