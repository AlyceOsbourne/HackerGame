# todo -> get __build_class__ working
from dataclasses import dataclass, field
from tkinter import DISABLED, Frame, VERTICAL, LEFT, Tk, Y, RIGHT, END, Text, NORMAL, font, Scrollbar
from typing import Any

import builtins_restricted
from reimplimented import *

intro_text = "### Welcome to the Average System Shell ###\nTo help fry your brain without frying your " \
             "computer\ncontrol enter to post code (yes this is temporary)\n\n "

__naughty_words__ = ["__builtins__", "__import__", "<CLASSNAME>", "<FUNCTIONNAME>", "<TYPE>", "<SUBTYPE>", "func_globals"]

@dataclass
class Level:
    name: str
    description: str
    level_filesystem: FileSystem
    level_globals: dict = field(default_factory=dict)


def logger_decorator(func):
    def out(*args, **kwargs):
        print(f"Entering Function: {func.__name__}, with args ({args}) and kwargs({kwargs})")
        ret = func(*args, **kwargs)
        if ret:
            print(f"-> Function: {func.__name__} yielded: {ret}", "\n")
        return ret

    return out


class Shell:
    __developer__ = """Alyce Osbourne,
github == https://github.com/AlyceOsbourne,
replit == https://replit.com/@AlyceOsbourne/HackerGame?v=1"""

    def update(self, *_):
        self.execute_input(self.grab_input())

    def grab_input(self) -> str:
        text = self.input_text.get(1.0, END).lstrip().replace("'", "\'").replace('"', '\"').rstrip()
        if text.endswith("\\"):
            text = text[:-1]
        self.input_text.delete(1.0, END)
        self.input_text.mark_set("insert", "%d.%d" % (1., 1.))
        return text

    def execute_input(self, string: str):
        if not string:
            return
        for w in __naughty_words__:
            if w in string:
                self.output_text.config(state=NORMAL)
                self.output_text.insert(END, "Don't be naughty! (┛ಠ_ಠ)┛彡┻━┻")
                self.output_text.config(state=DISABLED)
                return
        try:
            eval_res = eval(compile(string, "<stdin>", "eval"), self.__globals__)
            self.print_to_output(f"{string} == {eval_res}")
        except Exception:
            try:
                exec(compile(string, "<stdin>", "exec"), self.__globals__)
                self.print_to_output(string)
            except ModuleNotFoundError as error:
                self.print_to_output(string + " -> " + f"{error.__class__.__name__}: {error}")
            except Exception as error:
                self.print_to_output(string + " -> " + f"{repr(error)}")
                raise
        finally:
            print("\n")

    def print_to_output(self, *string, sep="\n"):
        self.output_text.config(state=NORMAL)
        for s in string:
            for r in s.split("\n"):
                self.output_text.insert(END, f" >>> " + r + sep)
        # self.output_text.insert(END, "\n")
        self.output_text.config(state=DISABLED)

    @staticmethod
    def import_module(self, *args):
        self.print_to_output("Importing ", *args)
        return None

    window = Tk()
    window.title("Shell")
    window.resizable(False, False)
    window.configure()
    font = font.Font()
    output_frame, input_frame = Frame(window), Frame(window)
    output_text = Text(output_frame, height=15, width=70, bg="black", fg="green")
    output_scroll = Scrollbar(output_frame, orient=VERTICAL, bg='black', command=output_text.yview)
    input_text = Text(input_frame, height=5, width=70, insertwidth=3, bg="black", fg="green",
                      insertbackground="green", tabs=font.measure("    "))
    input_scroll = Scrollbar(input_frame, orient=VERTICAL, bg='black', command=input_text.yview)
    output_frame.pack(pady=3, padx=3)
    output_text.pack(side=LEFT)
    output_scroll.pack(fill=Y, side=RIGHT)
    input_frame.pack()
    input_text.pack(side=LEFT)
    input_scroll.pack(fill=Y, side=RIGHT)

    __game__globals__ = dict(__name__="Shell", __builtins__=builtins_restricted, __developer__=__developer__)

    def __init__(self, level: Level = None):
        self.level_name = f"Mission {level.name}" if level else ""
        self.__globals__ = dict(**self.__game__globals__, **level.level_globals, ) if level else self.__game__globals__
        self.output_text.insert(END, intro_text)
        self.output_text.config(state=DISABLED)
        self.input_text.bind('<Control-Return>', self.update)
        self.window.mainloop()


if __name__ == "__main__":
    Shell()
