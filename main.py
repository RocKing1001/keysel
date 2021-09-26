from keysel.questions import choiceques
from keysel import qprompt

ques1 = choiceques("are you gay", ["yes", "no"], "no")

qprompt(ques1.testing(), ["c", "r", "h"])

