from tkinter import *
from rich import print
import builtins_restricted


def logger_decorator(func):
    def out(*args, **kwargs):
        print(f"Entering Function: {func.__name__}, with args ({args}) and kwargs({kwargs})")
        ret = func(*args, **kwargs)
        if ret:
            print(f"-> Function: {func.__name__} yielded: {ret}", "\n\r")
        return ret

    return out


__game__globals__ = dict(__name__="Shell", __builtins__=builtins_restricted)


class Shell:

    def update(self, *_):
        self.execute_input(self.grab_input())

    def grab_input(self) -> str:
        text = self.input_text.get(1.0, END).replace("'", '"').replace('"', '\"').strip(" ")
        text.replace("print(", "self.print(")
        self.input_text.delete(1.0, END)
        return text

    def execute_input(self, string: str):
        try:
            eval_res = eval(string, self.__globals__)
            self.print(f"{string} = {eval_res}" + "\n\r")
        except Exception:
            try:
                exec(string, self.__globals__)
                self.print(string + "\n\r")
            except Exception as error:
                self.print(string + "\n\t" + f"{error.__class__.__name__}: {error}" + "\n\r")
                raise

    def print(self, *string, sep="\n\r"):
        self.output_text.config(state=NORMAL)
        for s in string:
            self.output_text.insert(END, s+sep)
        self.output_text.config(state=DISABLED)

    def __init__(self, level=None):
        self.__globals__ = dict(**__game__globals__, **level) if level else __game__globals__
        self.window = Tk()
        self.window.title("Shell")
        self.window.resizable(False, False)
        self.window.configure()
        self.output_frame, self.input_frame = Frame(self.window), Frame(self.window)
        self.output_text = Text(self.output_frame, state=DISABLED, height=30, width=100, bg="black", fg="green")
        self.output_scroll = Scrollbar(self.output_frame, orient=VERTICAL, bg='black', command=self.output_text.yview())
        self.input_text = Text(self.input_frame, height=10, width=100, insertwidth=3, bg="black", fg="green",
                               insertbackground="green")
        self.input_scroll = Scrollbar(self.input_frame, orient=VERTICAL, bg='black', command=self.input_text.yview())
        self.output_frame.pack(pady=3, padx=3)
        self.output_text.pack(side=LEFT)
        self.output_scroll.pack(fill=Y, side=RIGHT)
        self.input_frame.pack()
        self.input_text.pack(side=LEFT)
        self.input_scroll.pack(fill=Y, side=RIGHT)
        self.input_text.bind('<Control-Return>', self.update)

        self.print(
            """
    Welcome to the Oops I Broke It Interactive Shell
    Where you can play around, screw up, and not blow up your 
    PC while you learn.   
        """+"\n\r"
        )


        self.window.mainloop()



if __name__ == "__main__":
    Shell()
