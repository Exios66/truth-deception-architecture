---
icon: readme
---

# RNG Results README Documentation

## Last Updated: 01.03.25

## Overview

The `csv` subdirectory within the RNG Results directory contains the primary data files generated from various random number generation (RNG) experiments. These datasets are crucial for the analysis of experimental conditions, including statistical validation, subject analysis, and algorithmic evaluation.

## Subdirectory Structure

```bash
csv/
├── EC-0-5.csv
├── EC-1-5.csv
├── EC-1-6.csv
├── subjects-csv/
│   └── 50_subject.csv
└── README.md
```

## Files and Folders

| File/Folder      | Description                                                                                            |
| ---------------- | ------------------------------------------------------------------------------------------------------ |
| `EC-0-5.csv`     | Contains results for the RNG experiment conducted under experimental condition 0.                      |
| `EC-1-5.csv`     | Contains results for the RNG experiment conducted under experimental condition 1 with configuration 5. |
| `EC-1-6.csv`     | Contains results for the RNG experiment conducted under experimental condition 1 with configuration 6. |
| `subjects-csv/`  | Subfolder containing CSV files specific to subject-level analysis.                                     |
| `50_subject.csv` | Subject-level data for an experiment involving 50 participants.                                        |
| `README.md`      | This documentation file.                                                                               |

## Purpose

The csv subdirectory supports the following objectives:

### 1. Centralized Data Storage

* Consolidates experimental RNG results and subject-level data in a standardized format.

### 2. Facilitate Analysis

* Provides researchers and contributors with datasets for statistical evaluation, algorithm refinement, and experiment reproducibility.

### 3. Subject Analysis

* The subjects-csv folder includes data relevant to participant-level insights and behavioral trends.

## Key Features

### 1. RNG Experimental Data

* Each EC-X-Y.csv file represents the results from a specific experimental condition (X) and configuration (Y).
* Includes columns for timestamp, generated values, and metadata (e.g., seeds, algorithms).

### 2. Subject-Level Data

* Files in the subjects-csv folder provide focused datasets on individual or grouped participant behavior.
* Currently includes the 50\_subject.csv file for detailed analysis of an experiment involving 50 participants.

### 3. Standardized Format

* All files follow a consistent CSV structure for easy integration with analytical tools and programming libraries.

## Usage Instructions

### 1. Access the Files

Clone the repository and navigate to the subdirectory:

```bash
git clone https://github.com/Exios66/truth-deception-architecture.git
cd truth-deception-architecture/Experimental_Conditions/RNG_Results/csv
```

### 2. Analyzing Data

Use Python or similar tools to load and analyze data:

```python
import pandas as pd
data = pd.read_csv('EC-0-5.csv')

# For subject-level analysis:
subject_data = pd.read_csv('subjects-csv/50_subject.csv')
```

### 3. Visualization

* Generate charts or statistical summaries using tools like Matplotlib or Excel for enhanced insights.

## Contribution Guidelines

To contribute to this subdirectory:

### 1. Adding New Files

* Ensure CSV files follow the naming convention: `EC-[condition]-[configuration].csv` or are placed in `subjects-csv` for subject-specific data.

### 2. Documentation

* Update this README file with descriptions of newly added files.

### 3. Submission

* Submit a pull request detailing the purpose and content of the new data files.

## Contact Information

For inquiries or contributions, please reach out:

* GitHub Profile: [Exios66](https://github.com/Exios66)
* Business Email: [jackjburleson@proton.me](mailto:jackjburleson@proton.me)

## Acknowledgments

Special thanks to contributors and collaborators for their effort in creating and maintaining these datasets. The insights derived from this data are integral to advancing the Truth-Deception Architecture project.
