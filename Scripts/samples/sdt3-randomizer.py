import random

# Define the items with reverse scoring flag
items = [
    {"number": 1, "text": "It's not wise to tell your secrets.", "reverse": False},
    {"number": 2, "text": "People see me as a natural leader.", "reverse": False},
    {"number": 3, "text": "I like to get revenge on authorities.", "reverse": False},
    {"number": 4, "text": "I like to use clever manipulation to get my way.", "reverse": False},
    {"number": 5, "text": "I hate being the center of attention.", "reverse": True},
    {"number": 6, "text": "I avoid dangerous situations at all costs.", "reverse": True},
    {"number": 7, "text": "Whatever it takes, you must get the important people on your side.", "reverse": False},
    {"number": 8, "text": "Many group activities tend to be dull without me.", "reverse": False},
    {"number": 9, "text": "Payback needs to be quick and nasty.", "reverse": False},
    {"number": 10, "text": "Avoid direct conflict with others because they may be useful in the future.", "reverse": False},
    {"number": 11, "text": "I know that I am special because everyone keeps telling me so.", "reverse": False},
    {"number": 12, "text": "People often say I’m out of control.", "reverse": True},
    {"number": 13, "text": "It's wise to keep track of information that you can use against people later.", "reverse": False},
    {"number": 14, "text": "I like to get acquainted with important people.", "reverse": False},
    {"number": 15, "text": "It’s true that I can be mean to others.", "reverse": False},
    {"number": 16, "text": "You should wait for the right time to get back at people.", "reverse": False},
    {"number": 17, "text": "I feel embarrassed if someone compliments me.", "reverse": True},
    {"number": 18, "text": "People who mess with me always regret it.", "reverse": False},
    {"number": 19, "text": "There are things you should hide from other people because they don't need to know.", "reverse": False},
    {"number": 20, "text": "I have been compared to famous people.", "reverse": False},
    {"number": 21, "text": "I have never gotten into trouble with the law.", "reverse": True},
    {"number": 22, "text": "Make sure your plans benefit you, not others.", "reverse": False},
    {"number": 23, "text": "I am just an average person.", "reverse": True},
    {"number": 24, "text": "I enjoy having sex with people I hardly know.", "reverse": False},
    {"number": 25, "text": "Most people can be easily manipulated.", "reverse": False},
    {"number": 26, "text": "I insist on getting the respect I deserve.", "reverse": False},
    {"number": 27, "text": "I'll say anything to get what I want.", "reverse": False}
]

# Function to randomize items
def randomize_items(item_list):
    randomized = item_list.copy()
    random.shuffle(randomized)
    return randomized

# Function to administer the assessment
def administer_assessment(randomized_items):
    responses = {}
    for item in randomized_items:
        print(f"Q{item['number']}: {item['text']}")
        # Here you would collect the user's response, e.g., on a scale from 1 to 5
        # For demonstration, we'll simulate with a placeholder
        response = input("Your response (1-5): ")
        responses[item['number']] = int(response)
    return responses

# Function to score the assessment
def score_assessment(responses, item_list):
    total_score = 0
    for item in item_list:
        score = responses.get(item['number'], 0)
        if item['reverse']:
            # Assuming a 5-point Likert scale
            score = 6 - score
        total_score += score
    return total_score

# Example Usage
if __name__ == "__main__":
    randomized = randomize_items(items)
    responses = administer_assessment(randomized)
    total = score_assessment(responses, items)
    print(f"Your total Dark Triad score is: {total}")
