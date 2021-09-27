from keysel.questions import choiceques
from keysel import qprompt

ques1 = choiceques("The answer is c", ["c", "r", "h"], "c")

ques1.inptAns(qprompt(ques1.getques(), ["c", "r", "h"]), {"key":"h", "help": "PRESS C to answer CISC\nPRESS R to answer RISC"})

