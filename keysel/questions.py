from keysel.exceptions import CorrectNotInChoices
from getch import getch

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
    def inptAns(self, prompt, help=None):
        self.prompt = prompt
        print(f"[?] {self.prompt}")

        char = str(getch()).lower()

        if char in self.choices:

            print(f"\033[A\033[{len(self.question)+5}C[{char}]\033[K")

            if help and char == help["key"]:
                print('\033[1m'+help["help"])
                print('\033[0m'+"Answer: ")
                char = str(getch()).lower()

                if char == self.correct:
                    print("You are right")
                else:
                    print("you are wrong")
                    
            elif char == self.correct:
                print("You are right")
            else:
                print("you are wrong")
        else:
            print("tbd, you inputted invalid key")
