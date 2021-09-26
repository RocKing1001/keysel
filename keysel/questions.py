from keysel.exceptions import CorrectNotInChoices

class choiceques():
    def __init__(self, question, choices, correct=None):
        self.question = question
        self.choices = choices
        self.correct = correct
    def getques(self):
        try:
            if self.correct not in self.choices and self.correct != None:
                raise CorrectNotInChoices()
            return self.question
        except CorrectNotInChoices:
            return "Correct choice is not present in choices"
    def inptans(self, prompt):
        self.prompt = prompt