# Q7. Create an abstract class Question with an abstract method evaluate_answer(). Derive MCQQuestion, TrueFalseQuestion, and DescriptiveQuestion. Implement answer evaluation for each question type.

from abc import ABC, abstractmethod

class Question(ABC):
    @abstractmethod
    def evaluate_answer(self, answer):
        pass

class MCQQuestion(Question):
    def __init__(self, correct_answer):
        self.correct_answer = correct_answer

    def evaluate_answer(self, answer):
        if answer == self.correct_answer:
            return "Correct Answer"
        else:
            return "Wrong Answer"

class TrueFalseQuestion(Question):
    def __init__(self, correct_answer):
        self.correct_answer = correct_answer

    def evaluate_answer(self, answer):
        if answer == self.correct_answer:
            return "Correct Answer"
        else:
            return "Wrong Answer"

class DescriptiveQuestion(Question):
    def __init__(self, correct_answer):
        self.correct_answer = correct_answer

    def evaluate_answer(self, answer):
        if answer.lower() == self.correct_answer.lower():
            return "Correct Answer"
        else:
            return "Answer needs evaluation"

mcq = MCQQuestion("B")
true_false = TrueFalseQuestion("True")
descriptive = DescriptiveQuestion("Python is a programming language")

print("MCQ:", mcq.evaluate_answer("B"))
print("True/False:", true_false.evaluate_answer("True"))
print("Descriptive:", descriptive.evaluate_answer("Python is a programming language"))