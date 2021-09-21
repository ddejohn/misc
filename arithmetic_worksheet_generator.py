import random
from dataclasses import dataclass


@dataclass
class Problem:
    prompt: str
    answer: int


class ArithmeticProblemSet:
    def __init__(self, num_problems: int = 100, difficulty=0) -> None:
        if type(num_problems) != int or not (5 <= num_problems):
            err = "Parameter `num_problems` must be an integer greater than 5!"
            raise ValueError(err)
        if type(difficulty) != int or not (0 <= difficulty <= 3):
            err = "Parameter `difficulty` must be an integer from 0 to 3!"
            raise ValueError(err)

        self.lim = {0: 10, 1: 25, 2: 50, 3: 100}[difficulty]
        self.scores = []
        self.problems = []
        self.num_problems = num_problems
        self.problem_types = (self.addition,
                              self.subtraction,
                              self.multiplication,
                              self.division)
        for _ in range(self.num_problems):
            self.problems.append(self.random_problem())

    def __str__(self, ans=False):
        return "\n".join(f"{p.prompt}{f' = {p.answer}'*ans}" for p in self.problems)

    def quiz(self):
        num_correct = 0
        quiz_len = self.num_problems // 5
        challenges = random.sample(self.problems, k=quiz_len)
        for idx, challenge in enumerate(challenges, 1):
            prompt = f"{idx})  {challenge.prompt}"
            if self.get_input(prompt) == challenge.answer:
                num_correct += 1
                print("\nCorrect!\n")
            else:
                print("\nIncorrect :(\n")
        print(f"Quiz completed! Correct: {num_correct}/{quiz_len}")
        self.scores.append(round(num_correct / quiz_len, 2))

    def random_problem(self):
        a, b = random.randint(0, self.lim), random.randint(0, self.lim)
        return random.choice(self.problem_types)(a, b)

    def addition(self, a, b):
        return Problem(f"{a} + {b}", a + b)

    def subtraction(self, a, b):
        return Problem(f"{a} - {b}", a - b)

    def multiplication(self, a, b):
        return Problem(f"{a} * {b}", a * b)

    def division(self, a, b):
        divisor, quotient = random.sample((a, b), 2)
        return Problem(f"{a * b} / {divisor}", quotient)

    def get_input(self, prompt: str) -> int:
        while True:
            try:
                user_input = int(input(f"{prompt} = "))
                break
            except ValueError:
                print("\nInvalid input type! Input should be an integer!\n")
        return user_input


q = ArithmeticProblemSet()
