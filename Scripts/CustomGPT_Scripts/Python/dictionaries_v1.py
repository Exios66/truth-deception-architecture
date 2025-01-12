import re

# Define keyword dictionaries for each subject
subject_dictionaries = {
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
            "proof", "trigonometry", "vector", "integral", "derivative", "shape", "angle"
        ],
        "description": "Mathematics and Geometry"
    }
}

# Function to assess input and select the appropriate subject
def assess_input(prompt):
    # Normalize and tokenize the input
    prompt = prompt.lower()
    matched_subject = None
    matched_keywords = []

    # Iterate through each subject's dictionary and match keywords
    for subject, data in subject_dictionaries.items():
        keywords = data["keywords"]
        matches = [word for word in keywords if re.search(r'\b' + re.escape(word) + r'\b', prompt)]
        
        if matches:
            matched_subject = subject
            matched_keywords = matches
            break

    # If no subject matched, return default response
    if not matched_subject:
        return {
            "subject": None,
            "description": "No relevant subject identified",
            "keywords": []
        }

    # Return subject and matching details
    return {
        "subject": matched_subject,
        "description": subject_dictionaries[matched_subject]["description"],
        "keywords": matched_keywords
    }

# Example usage
if __name__ == "__main__":
    # Sample prompts to test
    sample_prompts = [
        "What is the theory of relativity?",
        "Can you explain the structure of a neuron?",
        "Tell me about the Roman Empire's influence on modern culture.",
        "What are some examples of metaphors in Shakespeare's plays?",
        "How do you calculate the area of a triangle?"
    ]

    # Process each prompt and display results
    for prompt in sample_prompts:
        result = assess_input(prompt)
        print(f"Prompt: {prompt}")
        print(f"Subject: {result['description']}")
        print(f"Keywords Found: {result['keywords']}")
        print("-" * 50)