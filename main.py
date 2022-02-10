import tkinter
from tkinter import *
from itertools import count
from rich import print

def logger_decorator(func):
    def out(*args, **kwargs):
        print(f"Entering Function: {func.__name__}, with args ({args}) and kwargs({kwargs})")
        ret = func(*args, **kwargs)
        if ret:
            print(f"-> Function: {func.__name__} yielded: {ret}", "\n\r")
        return ret
    return out

window = Tk()
window.title("TB-RPG")

output_frame = Frame(window)
output_text, output_scroll, input_text = Text(output_frame, state=DISABLED, height=30, width= 100, insertwidth=1), Scrollbar(output_frame, orient=VERTICAL), Text(height=10, width=100, insertwidth=1)

output_frame.pack(pady=3, padx=3), output_text.pack(side=LEFT), output_scroll.pack(fill=Y, side=RIGHT), input_text.pack()

input_text.insert(END, "def addition(a, b):\n\treturn a+b")

__game__globals__ = {g:v for g, v in globals().items() if g in ["__name__", "__doc__", "__file__", "__builtins__"]}

def update_output(string):
    output_text.config(state=NORMAL)
    output_text.insert(END, string)
    output_text.config(state=DISABLED)

@logger_decorator
def grab_input() -> str:
    text = input_text.get(1.0, END)
    input_text.delete(1.0, END)
    return text

def execute_input(string: str):
    if string.__contains__("import "):
        pass  # todo special handling for import
    elif string.__contains__("with open") or string.__contains__("open("):
        pass  # todo special handling for open()
    else:
        try:
            update_output(f"{string} = {eval(string, __game__globals__)}")
        except Exception:
            try:
                exec(string, __game__globals__)
                update_output(string)
            except Exception as error:
                update_output(string+"\n\t"+f"{error.__class__.__name__}: {error}")
                raise
        update_output("\n\r")

def update(*args):
    execute_input(grab_input())

window.bind('<Control-Return>', update)
window.mainloop()