####### VIRTUAL MACHINE ########

current = None              # current executing VM (last defined)
target  = None              # target VM will be used by compiler

class VM:
    reg = {}                                # created VMs registry /static/
    def __init__(self, Name, Memory=[]):
        self.name = Name                    # VM name
        self.M = Memory                     # bytecode memory
        self.Ip = 0                         # instruction pointer (PC)
        self.Cp = 0                         # compiler pointer
        self.reg[Name] = self               # register created VM
    def head(self): return 'vm:%s'%self.name
    def dump(self):
        return self.head()+' M:%s Ip:%.4X Cp:%.4X'%(self.M,self.Ip,self.Cp)
    def __repr__(self): return self.dump()

########## COMPILER ############ 

import ply.lex  as lex
import ply.yacc as yacc

tokens = ['SYM','pVM']

t_ignore = ' \t\r'
t_ignore_COMMENT = r'\#.*'
def t_newline(t):
    r'\n'
    t.lexer.lineno += 1
    
def t_pVM(t):
    r'\.[vV][mM]'
    return t

def t_SYM(t):
    r'[a-zA-Z0-9_]+'
    return t
    
def t_error(t): raise BaseException(t)
lex.lex()

def p_REPL_none(p): ' REPL : '
def p_REPL_recur(p):
    ' REPL : REPL ex '
    print p[2]
def p_ex_SYM(p):
    ' ex : SYM '
    p[0] = p[1]
def p_ex_VM(p):
    ' ex : pVM SYM '
    current = target = VM(p[2]) ; print current ; print VM.reg
    
def p_error(p): raise BaseException(p)
yacc.yacc(debug=False,write_tables=False).parse(open('src.src').read())
