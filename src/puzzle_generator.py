import random
import time

class PuzzleGenerator:
    def __init__(self):
        self.levels = ["Easy", "Medium", "Hard"]

    def generate(self, difficulty):
        if difficulty == "Easy":
            a, b = random.randint(1, 10), random.randint(1, 10)
            op = random.choice(['+', '-'])
        elif difficulty == "Medium":
            a, b = random.randint(10, 50), random.randint(1, 10)
            op = random.choice(['+', '-', '*'])
        else:  # Hard
            a, b = random.randint(10, 100), random.randint(2, 10)
            op = random.choice(['*', '/'])

        question = f"{a} {op} {b}"
        answer = eval(f"{a} {op} {b}")  # Simple eval for basic math
        return question, round(answer, 2)
