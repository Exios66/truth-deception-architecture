#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
Subject Classification Script for GPT Knowledge Base Integration

This script classifies user prompts into subjects, leveraging keyword-based detection
across multiple knowledge domains (e.g., Astronomy & Physics, Neuroscience & Psychology, etc.).
It is designed to be integrated into a GPT-based system that references an external
subjects.csv file or any other knowledge base files for more nuanced handling.

Features:
1. Robust keyword detection for each subject category.
2. Immediate subject matching upon the first occurrence of relevant keywords.
3. Extended commentary and docstrings for maintainability.
4. Example usage demonstrating basic input prompts and subject classification.

Note: 
- Modify and expand 'SUBJECT_DICTIONARIES' to align with your CSV or any external references.
- This script stops after matching the first subject with relevant keywords. 
  If you prefer multiple subject matches, adjust the logic accordingly.
"""

import re

# ---------------------------------------------------------------------
# 1. SUBJECT DICTIONARIES
# ---------------------------------------------------------------------
# In production, you may load these from a CSV or database. Here, we provide
# a static reference dictionary for demonstration. Adjust as needed.
SUBJECT_DICTIONARIES = {
    "astronomy_physics": {
        "keywords": [
            "planet", "star", "galaxy", "black hole", "quantum", "relativity",
            "gravitational", "space", "astronomy", "physics", "cosmos", "orbit"
        ],
        "description": "Astronomy and Physics"
    },
    "neuroscience_psychology": {
        "keywords": [
            "brain", "neuron", "cognition", "behavior", "psychology",
            "neuroscience", "memory", "emotion", "mental", "mind", "perception"
        ],
        "description": "Neuroscience and Psychology"
    },
    "history_geography": {
        "keywords": [
            "history", "geography", "war", "empire", "civilization", "dynasty",
            "exploration", "continent", "culture", "archaeology", "migration", "map"
        ],
        "description": "History and Geography"
    },
    "literature_grammar": {
        "keywords": [
            "poetry", "prose", "grammar", "syntax", "novel", "author",
            "rhetoric", "metaphor", "language", "literature", "verse", "essay"
        ],
        "description": "Literature and Grammar"
    },
    "mathematics_geometry": {
        "keywords": [
            "algebra", "geometry", "calculus", "equation", "theorem",
            "proof", "trigonometry", "vector", "integral", "derivative",
            "shape", "angle"
        ],
        "description": "Mathematics and Geometry"
    }
}


# ---------------------------------------------------------------------
# 2. ASSESS INPUT
# ---------------------------------------------------------------------
def assess_input(prompt):
    """
    Takes a user prompt (string) and returns a dictionary with the matched subject,
    the subject's description, and any keywords found in that prompt.

    :param prompt: str, The user-provided question or statement.
    :return: dict, Contains:
        {
            "subject": str or None,
            "description": str,
            "keywords": list of str
        }
    """
    normalized_prompt = prompt.lower()

    # By default, no subject is matched
    matched_subject = None
    matched_keywords = []

    # Check each subject for keyword matches
    for subject, data in SUBJECT_DICTIONARIES.items():
        # For each keyword, use a regex word boundary check
        matches = [
            word
            for word in data["keywords"]
            # Example: re.search(r'\bgeometry\b', prompt)
            if re.search(r'\b' + re.escape(word.lower()) + r'\b', normalized_prompt)
        ]

        # If we find any matches, set the subject
        if matches:
            matched_subject = subject
            matched_keywords = matches
            break  # Stop after the first subject match

    if matched_subject:
        return {
            "subject": matched_subject,
            "description": SUBJECT_DICTIONARIES[matched_subject]["description"],
            "keywords": matched_keywords
        }

    # If no matches found at all
    return {
        "subject": None,
        "description": "No relevant subject identified",
        "keywords": []
    }


# ---------------------------------------------------------------------
# 3. EXAMPLE USAGE
# ---------------------------------------------------------------------
if __name__ == "__main__":
    sample_prompts = [
        "What is the theory of relativity?",
        "Can you explain the structure of a neuron?",
        "Tell me about the Roman Empire's influence on modern culture.",
        "What are some examples of metaphors in Shakespeare's plays?",
        "How do you calculate the area of a triangle?",
        "Which star is nearest to Earth?"
    ]

    for prompt in sample_prompts:
        result = assess_input(prompt)
        print(f"Prompt:          {prompt}")
        print(f"Matched Subject: {result['subject']}")
        print(f"Description:     {result['description']}")
        print(f"Keywords Found:  {result['keywords']}")
        print("-" * 70)