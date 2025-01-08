---
hidden: true
---

# Changelog - The Neural Architecture Underpinning Truth and Deception Detection

All notable changes to this project will be documented in this file.

## \[Unreleased]

### Added

* Survey Materials comprehensive documentation
  * FAD-Plus Scale implementation
  * AI Opinion Survey framework
  * Big Five Inventory integration
  * Cognitive Reflection Test setup
  * Need for Cognition Scale
  * Actively Open-minded Thinking Scale
* Scoring scripts for all personality measures
  * Data validation protocols
  * Quality control procedures
  * Automated scoring pipelines
* NASA-TLX implementation
  * Workload assessment tools
  * Analysis frameworks
  * Documentation structure
* Multi-platform deployment documentation
  * OpenRouter integration
  * SillyTavern setup guides
  * Claude API implementation
* External repository integration
  * Agentarium Framework setup
  * Claude Cookbook integration
  * Cline Development Tools

### Changed

* Enhanced documentation structure across all directories
* Updated Python script requirements and dependencies
* Improved README files with standardized formatting
* Restructured experimental conditions documentation

### Fixed

* Markdown linting errors (MD040) across documentation
* Code block language specifications
* Documentation formatting standardization
* File naming conventions
* Directory structure inconsistencies

## \[v0.1.8.5] - 2024-01-07

### Added

* Comprehensive survey implementation framework
* Advanced scoring system for personality measures
* Multi-platform deployment guidelines
* External repository documentation
* Enhanced API integration tools

### Changed

* Updated directory structure for better organization
* Enhanced documentation standards
* Improved code quality guidelines
* Standardized README formats

### Fixed

* Documentation inconsistencies
* File structure organization
* Naming convention compliance
* Cross-reference accuracy

## Assessment Tools

### Personality Measures

* Big Five Inventory (BFI)
* Cognitive Reflection Test (CRT)
* Need for Cognition Scale
* Actively Open-minded Thinking Scale

### Post-Interaction Assessments

* Perceived AI authenticity measures
* Trust and credibility evaluation
* Emotional response assessment
* Deception detection confidence

## Implementation Details

### Agentarium Framework

A comprehensive framework for developing and deploying AI agents.

### Key Features

* Agent orchestration
* Behavior modeling
* Multi-agent communication
* Performance analytics

### Implementation

```python
from agentarium import AgentFramework

# Initialize agent framework
agent = AgentFramework(
    model="claude-2",
    behavior_set="truth_analysis"
)

# Deploy agent
agent.deploy(
    task_parameters={
        "analysis_depth": "detailed",
        "verification_required": True
    }
)
```
