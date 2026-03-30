# mental_math_trainer/trainer.py
"""
Mental Math Trainer - Game logic
Generates questions, checks user answers, and tracks results.
"""

import random

def generate_questions(level: str, rounds: int = 5):
    """
    Generate a list of math questions based on difficulty level.
    Returns a list of tuples: (question_str, correct_answer)
    """
    questions = []
    for _ in range(rounds):
        if level == "easy":
            a = random.randint(1, 10)
            b = random.randint(1, 10)
            op = random.choice(["+", "-"])
        elif level == "medium":
            a = random.randint(10, 50)
            b = random.randint(1, 50)
            op = random.choice(["+", "-", "*"])
        elif level == "hard":
            a = random.randint(50, 100)
            b = random.randint(10, 100)
            op = random.choice(["+", "-", "*"])
        else:
            raise ValueError("Invalid difficulty level")

        question = f"{a} {op} {b}"
        answer = eval(question)
        questions.append((question, answer))
    return questions

def check_answers(user_answers, correct_answers):
    """
    Compare user input to correct answers.
    Returns a list of tuples: (question, user_input, correct_answer, status)
    Status is "correct", "wrong", or "invalid"
    """
    results = []
    for (question, correct), user_input in zip(correct_answers, user_answers):
        try:
            user_value = int(user_input)
            status = "correct" if user_value == correct else "wrong"
        except ValueError:
            user_value = user_input
            status = "invalid"
        results.append((question, user_input, correct, status))
    return results