# todo -> get __build_class__ working
import tkinter.font
from tkinter import *
import builtins_restricted

intro_text = "### Welcome to the Average System Shell ###\nTo help fry your brain without frying your computer\ncontrol enter to post code (yes this is temporary)\n"


def logger_decorator(func):
    def out(*args, **kwargs):
        print(f"Entering Function: {func.__name__}, with args ({args}) and kwargs({kwargs})")
        ret = func(*args, **kwargs)
        if ret:
            print(f"-> Function: {func.__name__} yielded: {ret}", "\n")
        return ret

    return out


class Shell:

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
        try:
            eval_res = eval(compile(string, "<stdin>", "eval"), self.__globals__)
            self.print_to_output(f">>> {string} == {eval_res}")
        except Exception:
            try:
                exec(compile(string, "<stdin>", "exec"), self.__globals__)
                self.print_to_output(">>> "+string)
            except Exception as error:
                self.print_to_output(">>> " + string + " -> " + f"{error.__class__.__name__}: {error}")
                raise
        finally:
            print("\n")

    def print_to_output(self, *string, sep=" "):
        self.output_text.config(state=NORMAL)
        for s in string:
            self.output_text.insert(END, s + sep)
        self.output_text.insert(END, "\n")
        self.output_text.config(state=DISABLED)

    @staticmethod
    def import_module(self, *args):
        self.print_to_output("Importing ", *args)
        return None

    window = Tk()
    window.title("Shell")
    window.resizable(False, False)
    window.configure()
    font = tkinter.font.Font()
    output_frame, input_frame = Frame(window), Frame(window)
    output_text = Text(output_frame, state=DISABLED, height=15, width=70, bg="black", fg="green")
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

    __game__globals__ = dict(__name__="Shell", __builtins__=builtins_restricted)

    def __init__(self, level=None):
        self.__globals__ = dict(**self.__game__globals__, **level, ) if level else self.__game__globals__
        builtins_restricted.session = self
        self.print_to_output(intro_text)
        self.input_text.bind('<Control-Return>', self.update)
        self.window.mainloop()


if __name__ == "__main__":
    Shell()
