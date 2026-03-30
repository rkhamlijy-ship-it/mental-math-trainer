import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))

from mental_math_trainer.trainer import generate_questions, check_answers

def test_generate_questions():
    questions = generate_questions("easy", 3)
    assert len(questions) == 3
    for q, a in questions:
        assert isinstance(q, str)
        assert isinstance(a, int)

def test_check_answers():
    questions = [("1 + 1", 2), ("2 + 2", 4)]
    user_answers = ["2", "5"]
    results = check_answers(user_answers, questions)
    assert results[0][3] == "correct"
    assert results[1][3] == "wrong"

def test_invalid_input():
    questions = [("1 + 1", 2)]
    user_answers = ["abc"]
    results = check_answers(user_answers, questions)
    assert results[0][3] == "invalid"