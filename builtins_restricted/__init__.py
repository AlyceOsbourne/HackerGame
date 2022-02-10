from builtins import *
for i in  ["compile", "eval", "exec", "open", "input"]:
    del globals()[i]
__all__ = [*globals().keys()]

