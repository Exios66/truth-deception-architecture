# Scripts Directory Documentation

## Last Updated 01.03.24

## Overview

This directory contains various utility scripts for question management, randomization, and number generation. The scripts are primarily written in Python and provide functionality for both command-line and GUI interfaces.

## Directory Structure

```bash
Scripts/
├── Python/
│   ├── random_number_generator.py
│   └── question-randomizer.py
├── samples/
│   └── sdt3-randomizer.py
└── README.md
```

## Script Descriptions

### Python Directory

#### random_number_generator.py

A comprehensive number selection utility that provides both CLI and GUI interfaces.

**Features:**

- Random number generation with configurable ranges
- Multiple randomization methods (Sample, Shuffle, Choices)
- Export capabilities (CSV, TXT)
- Logging functionality
- Seed setting for reproducibility
- Error handling and input validation
- GUI interface with Tkinter (optional)

#### question-randomizer.py

A question management system for handling and randomizing question databases.

**Features:**

- Loads questions from multiple source files
- Filters by difficulty and category
- Question validation
- Statistical analysis of question banks
- Exclusion list support
- Comprehensive logging

### Samples Directory

#### sdt3-randomizer.py

A specialized randomizer for psychological assessments.

**Features:**

- Randomizes assessment items
- Handles reverse-scored items
- Supports Likert scale responses
- Calculates total scores
- Built-in item database

## Usage Examples

### Random Number Generator

```bash
# CLI Mode
python random_number_generator.py

# GUI Mode
python random_number_generator.py --gui
```

### Question Randomizer

```python
from question_randomizer import QuestionRandomizer

# Initialize with question paths
randomizer = QuestionRandomizer({
    'Category': 'path/to/questions.csv'
})

# Get random questions
questions = randomizer.get_random_questions(
    count=3,
    difficulty=1,
    category='Physics'
)
```

## Dependencies

- Python 3.6+
- pandas
- tkinter (optional, for GUI)
- logging
- pathlib
- typing

## Installation

1. Ensure Python 3.6+ is installed
2. Install required packages:

```bash
pip install pandas
```

## Contributing

- Follow PEP 8 style guidelines
- Include appropriate error handling
- Add logging for significant operations
- Update documentation for new features
- Include type hints where appropriate

## License

[Insert License Information]

## Contact

[Insert Contact Information]
