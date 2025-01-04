# Agentarium Multi Agent Framework

https://github.com/Thytu/Agentarium

# 🌿 Agentarium

<div align="center">

[![License: Apache 2.0](https://img.shields.io/badge/license-Apache%202.0-yellow.svg)](https://opensource.org/licenses/Apache-2.0)
[![Python 3.10+](https://img.shields.io/badge/python-3.10+-blue.svg)](https://www.python.org/downloads/)
[![PyPI version](https://badge.fury.io/py/agentarium.svg)](https://badge.fury.io/py/agentarium)

A powerful Python framework for managing and orchestrating AI agents with ease. Agentarium provides a flexible and intuitive way to create, manage, and coordinate interactions between multiple AI agents in various environments.

[Installation](#installation) •
[Quick Start](#quick-start) •
[Features](#features) •
[Examples](#examples) •
[Documentation](#documentation) •
[Contributing](#contributing)

</div>

## 🚀 Installation

```bash
pip install agentarium
```

## 🎯 Quick Start

```python
from agentarium import Agent

# Create agents
agent1 = Agent(name="agent1")
agent2 = Agent(name="agent2")

agent1.talk_to(agent2, "Hello, how are you?")
agent2.talk_to(agent1, "I'm fine, thank you!")

agent1.act() # Same as agent.talk_to but it's the agent who decides what to do
```

## ✨ Features

- **🤖 Advanced Agent Management**: Create and orchestrate multiple AI agents with different roles and capabilities
- **🔄 Robust Interaction Management**: Coordinate complex interactions between agents
- **💾 Checkpoint System**: Save and restore agent states and interactions
- **📊 Data Generation**: Generate synthetic data through agent interactions
- **⚡ Performance Optimized**: Built for efficiency and scalability
- **🌍 Flexible Environment Configuration**: Define custom environments with YAML configuration files
- **🛠️ Extensible Architecture**: Easy to extend and customize for your specific needs

## 📚 Examples

### Basic Chat Example
Create a simple chat interaction between agents:

```python
# examples/basic_chat/demo.py
from agentarium import Agent

alice = Agent.create_agent()
bob = Agent.create_agent()

alice.talk_to(bob, "Hello Bob! I heard you're working on some interesting data science projects.")
bob.act()
```

### Synthetic Data Generation
Generate synthetic data through agent interactions:

```python
# examples/synthetic_data/demo.py
from agentarium import Agent
from agentarium.CheckpointManager import CheckpointManager

checkpoint = CheckpointManager("demo")

alice = Agent.create_agent()
bob = Agent.create_agent()

alice.talk_to(bob, "What a beautiful day!")
checkpoint.update(step="interaction_1")

checkpoint.save()
```

More examples can be found in the [examples/](examples/) directory.

## 📖 Documentation

### Environment Configuration
Configure your environment using YAML files:

```yaml
llm:
  provider: "openai" # any provider supported by aisuite
  model: "gpt-4o-mini" # any model supported by the provider

aisuite: # optional, credentials for aisuite
  openai:
    api_key: "sk-..."
```

### Key Components

- **Agent**: Base class for creating AI agents
- **CheckpointManager**: Handles saving and loading of agent states