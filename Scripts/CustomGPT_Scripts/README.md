# CustomGPT Scripts

![OpenAI GPT Logo](https://openai.com/content/images/2022/05/openai-avatar.png)

[![Python Version](https://img.shields.io/badge/python-3.8%2B-blue.svg)](https://www.python.org/downloads/)
[![OpenAI](https://img.shields.io/badge/OpenAI-API-green.svg)](https://openai.com/blog/openai-api)
[![Code Style](https://img.shields.io/badge/code%20style-PEP8-brightgreen.svg)](https://www.python.org/dev/peps/pep-0008/)
[![License](https://img.shields.io/badge/license-MIT-blue.svg)](LICENSE)

## Overview

This directory contains specialized Python scripts for interacting with OpenAI's GPT models in our research project. These scripts handle various aspects of GPT interaction, from prompt engineering to response analysis, specifically designed for truth and deception studies.

## Contents

- [Script Categories](#script-categories)
- [Installation](#installation)
- [Configuration](#configuration)
- [Usage Guidelines](#usage-guidelines)
- [Security](#-security)
- [Contributing](#-contributing)

## Script Categories

### Prompt Engineering

- `prompt_generator.py`: Dynamic prompt creation for different experimental conditions
- `context_builder.py`: Context management for maintaining conversation history
- `system_message_templates.py`: Template management for different GPT personas

### Response Analysis

- `response_analyzer.py`: Analysis of GPT responses for truth/deception markers
- `sentiment_tracker.py`: Tracking emotional content in responses
- `consistency_checker.py`: Verification of response consistency across conversations

### Experimental Controls

- `token_manager.py`: Management of API token usage and costs
- `rate_limiter.py`: Handling API rate limits and queuing
- `error_handler.py`: Graceful handling of API errors and timeouts

### Data Collection

- `response_logger.py`: Structured logging of all GPT interactions
- `metadata_collector.py`: Collection of interaction metadata
- `performance_metrics.py`: Tracking of response times and model performance

## Installation

```shell
# Navigate to CustomGPT Scripts directory
cd Scripts/CustomGPT_Scripts

# Install required dependencies
pip install -r requirements.txt

# Set up environment variables
cp .env.example .env
```

## Configuration

### API Setup

1. Obtain OpenAI API key from [OpenAI Platform](https://platform.openai.com)
2. Add API key to `.env` file:

```properties
OPENAI_API_KEY=your_api_key_here
MAX_TOKENS=2000
TEMPERATURE=0.7
```

### Model Settings

```python
DEFAULT_MODEL = "gpt-4"
FALLBACK_MODEL = "gpt-3.5-turbo"
MAX_RETRIES = 3
```

## Usage Guidelines

### Basic Usage

```python
from gpt_scripts import PromptGenerator, ResponseAnalyzer

# Initialize components
prompt_gen = PromptGenerator(model="gpt-4")
analyzer = ResponseAnalyzer()

# Generate and analyze response
response = prompt_gen.generate_prompt("deception_scenario_1")
analysis = analyzer.analyze_response(response)
```

### Best Practices

- Always use environment variables for API keys
- Implement proper error handling
- Monitor token usage
- Log all interactions
- Regular prompt template updates
- Validate responses before processing

## 🔒 Security

### Data Protection

- All API keys stored in environment variables
- Sensitive data encrypted at rest
- Regular security audits
- Rate limiting implementation
- Access control logging

### Compliance

- GDPR compliance measures
- Data retention policies
- Audit trail maintenance
- Regular security updates

## Directory Structure

```bash
CustomGPT_Scripts/
├── prompt_engineering/
│   ├── prompt_generator.py
│   ├── context_builder.py
│   └── templates/
│       ├── deception_scenarios/
│       └── truth_scenarios/
├── analysis/
│   ├── response_analyzer.py
│   ├── sentiment_tracker.py
│   └── consistency_checker.py
├── experimental/
│   ├── token_manager.py
│   ├── rate_limiter.py
│   └── error_handler.py
├── data_collection/
│   ├── response_logger.py
│   ├── metadata_collector.py
│   └── performance_metrics.py
├── utils/
│   ├── api_wrapper.py
│   └── config_manager.py
├── tests/
│   ├── test_prompts.py
│   └── test_analysis.py
└── config/
    ├── .env.example
    └── settings.py

```

## Related Documentation

- [OpenAI API Documentation](https://platform.openai.com/docs)
- [Implementation Guidelines](../Guidelines.md)
- [Security Protocols](../Security/README.md)
- [Data Collection Standards](../Data/README.md)

## Error Handling

Common error scenarios and solutions:

- Rate limiting: Implemented exponential backoff
- Token limits: Automatic text truncation
- API timeouts: Retry with fallback models
- Context length: Automatic context pruning

## Performance Optimization

- Batch processing for multiple requests
- Response caching for repeated queries
- Asynchronous processing capabilities
- Load balancing across API endpoints

---

## Last Updated: 01.03.25

For questions or updates, please contact the project maintainers.

## Version History

- v1.0.0 - Initial implementation
- v1.1.0 - Added response analysis tools
- v1.2.0 - Enhanced security features
- v1.3.0 - Performance optimizations

## 🤝 Contributing
