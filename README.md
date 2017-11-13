# RedCode Interpreter

This repo is a WIP for an implementation of the RedCode
pseudo-assembly language in Python. Specifically, using
the PLY module for lexing and parsing.

### Files

#### redcode.py

The main cli program. Takes a file-name of a redcode file to run.
Optionally, when provided a file of `-`, should read a program
from user input.

#### redcodeinterp.py

Code responsible for the interpretation of the generated output
from the parser. Before being interpreted, may be best to convert
the AST into a series of python objects.

#### redcodelex.py

Lexer, responsible for tokenizing the input stream.

#### redcodeobjs.py

Collection of python objects for representing the program.

#### redcodeparse.py

Code for parsing a token stream. Determines if the given input
is a syntactically-valid RedCode program. Then generates an
AST to be used for conversion into python objects.

For more information about redcode:
[Wiki page](https://en.wikibooks.org/wiki/Core_War/Redcode)
