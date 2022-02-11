import importlib

# import os  # needs new implement
# import sys  # needs new implement
# import math
# import json  # needs new implement
# import itertools
# import collections
# import more_itertools

from builtins import *
from builtins import __build_class__

allowed_modules = ["itertools", "math", "collections"]


def __import_module__(name, globals=None, locals=None, fromlist=(), level=0):
    print("Attempting import", name)
    if name in allowed_modules:
        try:
            return importlib.__import__(name, globals, locals, fromlist, level)
        except ModuleNotFoundError as m:
            print(m.name, m.msg)
    else:
        raise ModuleNotFoundError


def __build_class__restricted__():
    # todo class checks here, classes must not include outer access,
    #  an in some instances, if does replace with custom function
    return __build_class__


for i in ["compile", "eval", "exec", "open", "input", "print"]:  # these deleted methods need recreation
    del globals()[i]

globals()["__import__"] = __import_module__
globals()["__build_class__"] = __build_class__restricted__

__all__ = [k for k in globals().keys() if k not in ["allowed_modules"]]
