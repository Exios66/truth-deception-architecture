# Base Instructions Repository Documentation

## Overview

This directory contains the foundational instruction sets and behavioral guidelines for various chatbot profiles and interaction models. These instructions serve as the base layer for developing consistent, well-defined AI personalities and response patterns.

## Directory Structure

```
Base_Instructions/
├── instructions/        # Core instruction sets for different profiles
├── templates/          # Reusable instruction templates
└── common/            # Shared behavioral guidelines and rules
```

## Instruction Categories

### Universal Base Instructions
- Core behavioral guidelines
- Default fallback responses
- Context handling rules
- Professional communication standards

### Profile-Specific Instructions
- Unique personality traits
- Specialized knowledge domains
- Response patterns
- Interaction styles

## Usage Guidelines

1. **Implementation**
   - Instructions should be implemented hierarchically
   - Universal guidelines take precedence over profile-specific rules
   - Maintain consistency across different interaction contexts

2. **Maintenance**
   - Regular updates to reflect new requirements
   - Version control for instruction sets
   - Documentation of changes in CHANGELOG.md

3. **Quality Standards**
   - Clear and unambiguous directives
   - Consistent formatting
   - Regular validation and testing

## File Naming Convention

- Profile instructions: `{profile-name}-v{version}.md`
- Templates: `template-{type}-v{version}.md`
- Common guidelines: `common-{category}-v{version}.md`

## Version Control

- All instruction files are versioned (e.g., v1, v2)
- Major changes increment the version number
- Changes are documented in the root CHANGELOG.md

## Contributing

When adding or modifying instructions:
1. Follow the established formatting guidelines
1. Update version numbers appropriately
1. Document changes in CHANGELOG.md
1. Ensure backwards compatibility when possible 