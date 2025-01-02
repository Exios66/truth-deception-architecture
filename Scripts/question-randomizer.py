import pandas as pd
import random
from typing import Dict, List, Optional, Union
from pathlib import Path
import logging

# Configure logging
logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(levelname)s - %(message)s'
)

class QuestionRandomizer:
    """A class to handle question loading and randomization."""
    
    def __init__(self, question_paths: Dict[str, str]):
        """
        Initialize the QuestionRandomizer with paths to question files.
        
        Args:
            question_paths (Dict[str, str]): Dictionary mapping categories to file paths
        """
        self.question_paths = question_paths
        self.questions_df = self._load_all_data()
        self.categories = self.questions_df['Knowledge Category'].unique()
        self.difficulties = sorted(self.questions_df['difficulty'].unique())
    
    def _load_all_data(self) -> pd.DataFrame:
        """Load and combine data from all specified CSV files."""
        all_questions = []
        
        for category, path in self.question_paths.items():
            try:
                df = pd.read_csv(Path(path))
                df['source_file'] = path  # Track the source file
                all_questions.append(df)
                logging.info(f"Loaded {len(df)} questions from {path}")
            except Exception as e:
                logging.error(f"Error loading {path}: {str(e)}")
                continue
        
        if not all_questions:
            raise ValueError("No question files could be loaded")
        
        combined_df = pd.concat(all_questions, ignore_index=True)
        self._validate_questions(combined_df)
        return combined_df
    
    def _validate_questions(self, df: pd.DataFrame) -> None:
        """Validate the structure and content of questions."""
        required_columns = ['question', 'options', 'correct_answer', 'difficulty', 'Knowledge Category']
        missing_columns = [col for col in required_columns if col not in df.columns]
        
        if missing_columns:
            raise ValueError(f"Missing required columns: {missing_columns}")
        
        # Validate difficulty levels
        invalid_difficulties = df[~df['difficulty'].isin([0, 1, 2])]
        if not invalid_difficulties.empty:
            logging.warning(f"Found {len(invalid_difficulties)} questions with invalid difficulty levels")
    
    def get_random_questions(
        self,
        count: int = 1,
        difficulty: Optional[int] = None,
        category: Optional[str] = None,
        exclude_ids: Optional[List[int]] = None
    ) -> List[Dict]:
        """
        Get multiple random questions based on criteria.
        
        Args:
            count (int): Number of questions to return
            difficulty (Optional[int]): Difficulty level (0, 1, or 2)
            category (Optional[str]): Knowledge category
            exclude_ids (Optional[List[int]]): Question IDs to exclude
            
        Returns:
            List[Dict]: List of selected questions
        """
        filtered_df = self.questions_df.copy()
        
        if difficulty is not None:
            if difficulty not in self.difficulties:
                raise ValueError(f"Invalid difficulty. Must be one of {self.difficulties}")
            filtered_df = filtered_df[filtered_df['difficulty'] == difficulty]
        
        if category is not None:
            if category not in self.categories:
                raise ValueError(f"Invalid category. Must be one of {self.categories}")
            filtered_df = filtered_df[filtered_df['Knowledge Category'] == category]
        
        if exclude_ids:
            filtered_df = filtered_df[~filtered_df.index.isin(exclude_ids)]
        
        if filtered_df.empty:
            logging.warning("No questions match the specified criteria")
            return []
        
        # Ensure we don't try to get more questions than available
        count = min(count, len(filtered_df))
        selected = filtered_df.sample(n=count)
        
        return [self._format_question(row) for _, row in selected.iterrows()]
    
    def _format_question(self, row: pd.Series) -> Dict:
        """Format a question row into a standardized dictionary."""
        return {
            'id': row.name,
            'question': row['question'],
            'options': row['options'],
            'correct_answer': row['correct_answer'],
            'difficulty': row['difficulty'],
            'category': row['Knowledge Category'],
            'source': row['source_file']
        }
    
    def get_statistics(self) -> Dict:
        """Get statistics about the loaded questions."""
        return {
            'total_questions': len(self.questions_df),
            'categories': {
                cat: len(self.questions_df[self.questions_df['Knowledge Category'] == cat])
                for cat in self.categories
            },
            'difficulties': {
                diff: len(self.questions_df[self.questions_df['difficulty'] == diff])
                for diff in self.difficulties
            }
        }

def main():
    """Example usage of the QuestionRandomizer class."""
    # Example paths - update these to your actual file paths
    question_paths = {
        'Literature': 'data/Refined_Literature_Questions.csv',
        'Mathematics': 'data/Refined_Mathematics_Questions.csv'
    }
    
    try:
        # Initialize the randomizer
        randomizer = QuestionRandomizer(question_paths)
        
        # Print statistics
        stats = randomizer.get_statistics()
        print("\nQuestion Statistics:")
        print(f"Total Questions: {stats['total_questions']}")
        print("\nBy Category:")
        for cat, count in stats['categories'].items():
            print(f"{cat}: {count} questions")
        print("\nBy Difficulty:")
        for diff, count in stats['difficulties'].items():
            print(f"Level {diff}: {count} questions")
        
        # Example: Get 3 random questions of medium difficulty
        print("\nExample: 3 Medium Difficulty Questions")
        questions = randomizer.get_random_questions(count=3, difficulty=1)
        for i, q in enumerate(questions, 1):
            print(f"\nQuestion {i}:")
            print(f"Category: {q['category']}")
            print(f"Question: {q['question']}")
            print(f"Options: {q['options']}")
            
    except Exception as e:
        logging.error(f"Error in main: {str(e)}")

if __name__ == "__main__":
    main()