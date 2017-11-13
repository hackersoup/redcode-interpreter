import ply.lex as lex

tokens = [
    'ID',
    'IMMEDIATE',
    'SEMICOLON',
    'COLON',
    'COMMA',
]

reserved = {
    'DAT': 'DAT', # DAT B
    'MOV': 'MOV', # MOV A, B
    'ADD': 'ADD', # ADD A, B
    'SUB': 'SUB', # SUB A, B
    'JMP': 'JMP', # JMP B
    'JMZ': 'JMZ', # JMZ A, B
    'CMP': 'CMP', # CMP A, B
    'NOP': 'NOP', # NOP
}

tokens += list(reserved.values())

t_SEMICOLON = r'\;'
t_COLON = r'\:'
t_COMMA = r'\,'
#t_NEWLINE = r'\n+'
#t_WHITESPACE = r'[\t ]+'

# Ignore comments
t_ignore_COMMENT = r'\;.*'

# Ignore whitespace
t_ignore = r' \t'


def t_NEWLINE(t):
    r'\n+'
    pass

# Generic identifier token
def t_ID(t):
    r'[a-zA-Z0-9]+'
    t.type = reserved.get(t.value.upper(), 'IMMEDIATE')
    return t

# Support only for integer decimal immediates
def t_IMMEDIATE(t):
    r'\d+'
    t.value = int(t.value)
    return t

lexer = lex.lex()
