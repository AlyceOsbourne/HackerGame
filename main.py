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
        text = self.input_text.get(1.0, END)
        self.input_text.delete(1.0, END)
        return text

    def execute_input(self, string: str):
        if string.__contains__("import "):
            pass  # todo special handling for import
        elif string.__contains__("with open") or string.__contains__("open("):
            pass  # todo special handling for open()
        else:
            try:
                self.update_output(f"{string} = {eval(string, self.__globals__)}" + "\n\r")
            except Exception:
                try:
                    exec(string, self.__globals__)
                    self.update_output(string + "\n\r")
                except Exception as error:
                    self.update_output(string + "\n\t" + f"{error.__class__.__name__}: {error}" + "\n\r")
                    raise
            self.update_output("\n\r")

    def update_output(self, string):
        self.output_text.config(state=NORMAL)
        self.output_text.insert(END, string)
        self.output_text.config(state=DISABLED)

    def __init__(self, level=None):
        self.__globals__ = dict(**__game__globals__, **level) if level else __game__globals__
        self.window = Tk()
        self.window.title("TB-RPG")
        self.window.configure()
        self.output_frame, self.input_frame = Frame(self.window), Frame(self.window)
        self.output_text = Text(self.output_frame, state=DISABLED, height=30, width=100, bg="black", fg="green")
        self.output_scroll = Scrollbar(self.output_frame, orient=VERTICAL, bg='black')
        self.input_text = Text(self.input_frame, height=10, width=100, insertwidth=3, bg="black", fg="green",
                               insertbackground="green")
        self.input_scroll = Scrollbar(self.input_frame, orient=VERTICAL, bg='black')
        self.output_frame.pack(pady=3, padx=3)
        self.output_text.pack(side=LEFT)
        self.output_scroll.pack(fill=Y, side=RIGHT)
        self.input_frame.pack()
        self.input_text.pack(side=LEFT)
        self.input_scroll.pack(fill=Y, side=RIGHT)
        self.window.bind('<Control-Return>', self.update)
        self.window.mainloop()

        self.update_output("Welcome to the Oops I Broke It Interactive Shell")


if __name__ == "__main__":
    Shell()
