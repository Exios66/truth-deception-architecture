# Question Randomizer Instructions

## Overview

A Python class for managing and randomizing questions from multiple data sources with support for difficulty levels, categories, and exclusion criteria.

## Code Structure

```python
question-randomizer.py
├── Class: QuestionRandomizer
│   ├── Methods
│   │   ├── __init__()
│   │   ├── _load_all_data()
│   │   ├── _validate_questions()
│   │   ├── get_random_questions()
│   │   ├── _format_question()
│   │   └── get_statistics()
└── Function: main()
```

## Class Documentation

### QuestionRandomizer

```python
class QuestionRandomizer:
    def __init__(self, question_paths: Dict[str, str]):
        """
        Initialize randomizer with question file paths
        
        Args:
            question_paths: Dictionary mapping categories to file paths
        """
```

#### Core Methods

##### Loading & Validation

```python
def _load_all_data(self) -> pd.DataFrame:
    """
    Loads CSVs and combines into single DataFrame
    Returns: Combined DataFrame of all questions
    """

def _validate_questions(self, df: pd.DataFrame) -> None:
    """
    Validates DataFrame structure and content
    Required columns: 
    - question
    - options 
    - correct_answer
    - difficulty
    - Knowledge Category
    """
```

##### Question Retrieval

```python
def get_random_questions(
    self,
    count: int = 1,
    difficulty: Optional[int] = None,
    category: Optional[str] = None,
    exclude_ids: Optional[List[int]] = None
) -> List[Dict]:
    """
    Get random questions matching criteria
    
    Args:
        count: Number of questions
        difficulty: Level (0-2)
        category: Knowledge category
        exclude_ids: IDs to exclude
        
    Returns: List of question dictionaries
    """
```

## Usage Example

```python
# Initialize
question_paths = {
    'Literature': 'data/Refined_Literature_Questions.csv',
    'Mathematics': 'data/Refined_Mathematics_Questions.csv'
}

randomizer = QuestionRandomizer(question_paths)

# Get questions
questions = randomizer.get_random_questions(
    count=3,
    difficulty=1,
    category='Literature'
)

# Get statistics
stats = randomizer.get_statistics()
```

## Data Format

### Input CSV Requirements

- Required columns:
  - `question`: Question text
  - `options`: Answer options
  - `correct_answer`: Correct answer
  - `difficulty`: Level (0-2)
  - `Knowledge Category`: Subject area

### Output Question Format

```python
{
    'id': int,
    'question': str,
    'options': str,
    'correct_answer': str,
    'difficulty': int,
    'category': str,
    'source': str
}
```

## Dependencies

- pandas
- random
- typing
- pathlib
- logging

## Error Handling

- Logs errors for file loading issues
- Validates data structure
- Checks for invalid difficulty levels
- Handles missing/invalid categories

## Statistics

```python
stats = {
    'total_questions': int,
    'categories': Dict[str, int],
    'difficulties': Dict[int, int]
}
```

Would you like me to explain any specific part of the implementation in more detail?
