from keysel.exceptions import CorrectNotInChoices
from getch import getch
from prompt_toolkit import print_formatted_text as pt_prompt
from prompt_toolkit.formatted_text import FormattedText, ANSI
from prompt_toolkit.styles import Style

style = Style.from_dict({
    '': '#FFFFFF',
    "ques": "#FFFFFF bold",
    "ans": "#5C7AEA",
    "choices": "#808080",
    "tip": "",
    "icon": "#5C7AEA bold",
    "help": ""
})

class choiceques():
    def __init__(self, question, choices, correct=None, style=style):
        self.question = question
        self.choices = choices
        self.correct = correct
        self.style = style
    def getques(self):
        try:
            if self.correct not in self.choices and self.correct != None:
                raise CorrectNotInChoices()
            return self.question
        except CorrectNotInChoices:
            return "Correct choice is not present in choices"
    def inptAns(self, prompt, help=None, style_=None):
        self.prompt = prompt
        # print(f"[?] {self.prompt}")

        pt_prompt(FormattedText(self.prompt), style=self.style)
        char = str(getch()).lower()

        if char in self.choices:
            print(f"\x1b[A\x1b[{len(self.question)+1}C[{char}]\x1b[K")
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
