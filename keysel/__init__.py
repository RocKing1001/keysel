import getch

'''
Style: accepts rgb values for ques, ans, icon, tip, highlight
'''
style = {
    "ques": "\033[1;37m",
    "ans": "\033[1;34m",
    "tip": "\033[2;37m"
}

RESET = '\033[0m'
def qprompt(ques, style=style):
    qstyle = style["ques"].replace(" ", "")
    astyle = style["ans"].replace(" ", "")
    print(qstyle+ques+astyle, end="")
    char = getch.getch()
    print(char)