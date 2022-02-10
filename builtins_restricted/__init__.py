from builtins import *

exclude = ["compile", "eval", "exec", "open", "input"]

for i in exclude:
    del globals()[i]

__all__ = [*globals().keys()]