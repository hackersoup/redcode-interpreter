import ply.yacc as yacc
from redcodelex import tokens

# Debug?
DEBUG = True

# Parser tongue
start = 'program'

def p_program(p):
    '''program : directives
    '''
    if DEBUG: print("Match program")
    p[0] = ('PROGRAM', p[1])

def p_directives(p):
    '''directives : directive directives
                  | directive'''
    if len(p) == 3:
        p[0] = ('DIRECTIVE', p[1], p[2])
    elif len(p) == 2:
        p[0] = ('DIRECTIVE', p[1])

def p_directive_mov(p):
   '''directive : MOV IMMEDIATE COMMA IMMEDIATE'''
   if DEBUG: print("Match MOV")
   p[0] = ('MOV', p[2], p[4])

def p_directive_add(p):
    '''directive : ADD IMMEDIATE COMMA IMMEDIATE'''
    if DEBUG: print("Match ADD")
    p[0] = ('ADD', p[2], p[4])

def p_directive_nop(p):
    '''directive : NOP'''
    if DEBUG: print("Match NOP")
    p[0] = ('NOP')

def p_directive_sub(p):
    '''directive : SUB IMMEDIATE COMMA IMMEDIATE'''
    if DEBUG: print("Match SUB")
    p[0] = ('SUB', p[2], p[4])

def p_directive_jmp(p):
    '''directive : JMP IMMEDIATE'''
    if DEBUG: print("Match JMP")
    p[0] = ('JMP', p[2])

def p_directive_jmz(p):
    '''directive : JMZ IMMEDIATE COMMA IMMEDIATE'''
    if DEBUG: print("Match JMZ")
    p[0] = ('JMZ', p[2], p[4])

def p_directive_cmp(p):
    '''directive : CMP IMMEDIATE COMMA IMMEDIATE'''
    if DEBUG: print("Match CMP")
    p[0] = ('CMP', p[2], p[4])


def parse(data, debug=0):
    parser.error = 0
    p = parser.parse(data, debug=debug)
    if parser.error:
        return None
    return p


parser = yacc.yacc()
