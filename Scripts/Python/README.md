# Python Scripts README Documentation

## Last Updated 01.03.25

## Overview

This directory contains Python scripts essential to the Truth-Deception Architecture project's experimental and analytical processes.

## Directory Structure

```bash
Scripts/
├── README.md
├── question-randomizer.py
└── random_number_generator.py
```

## Script Descriptions

### question-randomizer.py

Script for randomizing question presentation during experimental trials.

#### Features

- Question pool randomization
- Balanced distribution algorithms
- Session-specific question sets
- Cross-condition randomization

### random_number_generator.py

Core RNG implementation for experimental conditions.

#### RNG Features

- True random number generation
- Configurable parameters
- Logging capabilities
- Experimental condition support

## Usage

### Question Randomizer

```python
# Example usage
python question-randomizer.py --pool-size 50 --session-id ABC123
```

### Random Number Generator

```python
# Example usage
python random_number_generator.py --condition EC-1-5 --trials 100
```

## Dependencies

- Python 3.8+
- NumPy
- Pandas
- SciPy

## Data Output

- CSV format
- Timestamped files
- Condition-specific folders
- Backup functionality

## Contact

For technical support or contributions:

- Repository: [Exios66](https://github.com/Exios66)
- Email: <jackjburleson@proton.me>
