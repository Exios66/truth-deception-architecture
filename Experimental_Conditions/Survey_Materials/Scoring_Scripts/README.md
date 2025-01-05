# Scoring Scripts in R README Documentation

## Last Updated: 01.03.25

## Overview

This directory contains R scripts for scoring and analyzing survey responses from the experimental conditions. The scripts are designed to process raw survey data and generate standardized scores across different measures.

## Files

- `scoring_template.R`: Main scoring script template with functions for all survey types

## Requirements

- R version 4.0.0 or higher
- Required packages:
  - tidyverse
  - psych
  - car
  - lme4
  - ggplot2
  - readxl

## Usage Instructions

### Data Preparation

1. Ensure data files are in CSV format
2. Follow naming convention: `YYYYMMDD_condition_surveytype.csv`
3. Place data files in the appropriate `/data` directory

### Running Scripts

```R
source("scoring_template.R")
process_survey_data(input_file, output_dir)
```

### Output Files

- Raw scores: `*_raw_scores.csv`
- Standardized scores: `*_std_scores.csv`
- Summary statistics: `*_summary.csv`
- Visualization plots: `*_plots.pdf`

## Scoring Methods

### Survey-Specific Scoring

1. Personality Measures
   - Big Five Inventory
   - Dark Triad
   - HEXACO

2. AI Opinion Survey
   - Trust in AI
   - Perceived Intelligence
   - Interaction Quality

3. NASA-TLX
   - Mental Demand
   - Physical Demand
   - Temporal Demand
   - Performance
   - Effort
   - Frustration

### Data Validation

- Missing data handling
- Outlier detection
- Reliability checks
- Consistency validation

## Quality Control

- Data integrity checks
- Score range validation
- Cross-validation procedures
- Error logging

## Troubleshooting

- Common errors and solutions
- Data format issues
- Package conflicts
- Memory management

## Contact

For technical issues or questions about the scoring procedures, contact:
- Technical Support: [Contact Information]
- Research Lead: [Contact Information]

## Version History

- v1.0.0 (01.03.25): Initial release
- Future versions will be documented here

## License

All scripts are proprietary and confidential to the research project.
Do not distribute without explicit permission.
