<div align="center">

# 🛠️ Scripts Directory Documentation

[![Last Update](https://img.shields.io/badge/Last%20Updated-01.03.24-blue?style=for-the-badge)](CHANGELOG.md)
[![Python Version](https://img.shields.io/badge/Python-3.6%2B-brightgreen?style=for-the-badge&logo=python)](https://www.python.org)
[![Code Style](https://img.shields.io/badge/Code%20Style-PEP%208-orange?style=for-the-badge)](https://www.python.org/dev/peps/pep-0008/)

</div>

## 📑 Contents
- [Overview](#-overview)
- [Directory Structure](#-directory-structure)
- [Script Descriptions](#-script-descriptions)
- [Usage Examples](#-usage-examples)
- [Setup](#-setup)
- [Contributing](#-contributing)

## 🔍 Overview

This directory contains utility scripts for question management, randomization, and number generation. The scripts are implemented in Python with both CLI and GUI interfaces, featuring comprehensive logging, error handling, and data validation.

## 📂 Directory Structure

```text
Scripts/
├── Python/
│   ├── random_number_generator.py    # Number generation utility
│   └── question_randomizer.py        # Question management system
├── samples/
│   └── sdt3_randomizer.py           # Psychological assessment tool
├── tests/                           # Unit and integration tests
│   └── test_randomizers.py
├── requirements.txt                 # Project dependencies
└── README.md                        # This documentation
```

## 📝 Script Descriptions

### 🐍 Python Directory

#### 1. `random_number_generator.py`

Advanced number generation utility with dual interfaces.

**Key Features:**
- 🎲 Multiple randomization algorithms
- 📊 Statistical distribution options
- 💾 Export to CSV/TXT formats
- 📱 GUI interface (Tkinter)
- 🔄 Reproducible results via seed setting
- 📋 Comprehensive input validation
- 📝 Detailed operation logging

#### 2. `question_randomizer.py`

Sophisticated question bank management system.

**Key Features:**
- 📚 Multi-source question loading
- 🏷️ Category and difficulty filtering
- ✅ Automated validation checks
- 📊 Question bank analytics
- ⚠️ Exclusion management
- 📝 Event logging
- 🔄 Custom randomization patterns

### 🧪 Samples Directory

#### `sdt3_randomizer.py`

Specialized psychological assessment tool.

**Key Features:**
- 🔄 Assessment item randomization
- ⚖️ Reverse-scoring support
- 📊 Likert scale processing
- 📈 Score calculation
- 💾 Built-in item database
- 📝 Result reporting

## 💻 Usage Examples

### Random Number Generator

```python
# CLI Mode
python random_number_generator.py --range 1 100 --count 10 --unique

# GUI Mode
python random_number_generator.py --gui
```

### Question Randomizer

```python
from question_randomizer import QuestionRandomizer

# Initialize randomizer
randomizer = QuestionRandomizer(
    question_paths={
        'General': 'questions/general.csv',
        'Technical': 'questions/technical.csv'
    },
    config={
        'logging_level': 'INFO',
        'validation': True
    }
)

# Generate question set
questions = randomizer.get_random_questions(
    count=5,
    difficulty_range=(1, 3),
    categories=['Technical'],
    exclude_ids=[101, 102]
)
```

## 🛠️ Setup

### Dependencies

```text
Python >= 3.6
pandas >= 1.3.0
numpy >= 1.19.0
tkinter (optional, for GUI)
pytest (development)
```

### Installation

```bash
# Clone repository
git clone https://github.com/Exios66/truth-deception-architecture.git

# Navigate to Scripts directory
cd truth-deception-architecture/Scripts

# Install dependencies
pip install -r requirements.txt
```

## 🤝 Contributing

1. Fork the repository
2. Create feature branch (`git checkout -b feature/NewFeature`)
3. Follow coding standards:
   - ✅ PEP 8 compliance
   - ✅ Type hints
   - ✅ Docstrings
   - ✅ Unit tests
   - ✅ Error handling
   - ✅ Logging
4. Commit changes (`git commit -m 'Add NewFeature'`)
5. Push to branch (`git push origin feature/NewFeature`)
6. Open Pull Request

## 📄 License

This project is licensed under the MIT License - see the [LICENSE](../LICENSE) file for details.

## 📞 Contact

- **Author**: Jack J Burleson
- **GitHub**: [@Exios66](https://github.com/Exios66)
- **Project Link**: [truth-deception-architecture](https://github.com/Exios66/truth-deception-architecture)

---

<div align="center">

**Part of the [Neural Architecture of Truth & Deception Project](https://github.com/Exios66/truth-deception-architecture)**

</div>
