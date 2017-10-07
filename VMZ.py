import sys ; sys.stdout = open('log.log','w')

####### VIRTUAL MACHINE ########

_bye = False                # stop system semaphore

current = None              # current executing VM (last defined)
target  = None              # target VM will be used by compiler

class UnknownCommand(BaseException): pass

class VM:
    reg = {}                                    # created VMs registry /static/
    Msz = 0x100                                 # max memory size limit
    def __init__(self, Name, Memory):
        self.name = Name                        # VM name
        self.M = Memory                         # bytecode memory
        self.Ip = 0                             # instruction pointer (PC)
        self.S = [] ; self.Sp=0;                # data stack
        self.R = [] ; self.Rp=0;                # return stack
        self.Cp = 0                             # compiler pointer
        self.reg[Name] = self                   # register created VM
        self.V = {}                             # method [V]ocabulary
    def head(self): return 'vm:%s' % self.name
    def dump(self):
        return self.head()+' M:%s Ip:%.4X Cp:%.4X V:%s'%(self.M,self.Ip,self.Cp,self.V)
    def __repr__(self): return self.dump()
    def compile(self, CMD):
        ' compile command '
        self.M.append(CMD) ; self.Cp += 1 ; assert self.Cp < self.Msz
    ticks = 0        
    def tick(self):
        self.ticks += 1
        if self.ticks > 0x10: raise BaseException('too long')
        ' interpreter loop: do one command '
        assert self.Ip<self.Cp ; C = self.M[self.Ip] ; self.Ip +=1  # FETCH
        if C == 'nop' : pass
        elif C == 'bye' : global _bye ; _bye = True
        elif C == 'ret' : self.Ip = self.R.pop() ; self.Rp-=1
        elif C[0] == 'jmp': self.Ip = C[1]
        else: raise UnknownCommand(C)         

########## COMPILER ############ 

import ply.lex  as lex
import ply.yacc as yacc

tokens = ['SYM','pVM','CMD','COLON','SEMICOLON','BEGIN','AGAIN']

t_ignore = ' \t\r'
t_ignore_COMMENT = r'\#.*'
def t_newline(t):
    r'\n'
    t.lexer.lineno += 1
    
def t_COLON(t):
    r'\:'
    return t
def t_SEMICOLON(t):
    r'\;'
    return t
    
def t_pVM(t):
    r'\.[vV][mM]'
    return t

def t_BEGIN(t):
    r'begin'
    return t
def t_AGAIN(t):
    r'again'
    return t

def t_CMD(t):
    r'(nop|bye)'
    return t

def t_SYM(t):
    r'[a-zA-Z0-9_]+'
    return t
    
def t_error(t): raise SyntaxError(t)
lexer = lex.lex()                                   # create lexer

def p_REPL_none(p): ' REPL : '
def p_REPL_VM(p):
    ' REPL : REPL pVM SYM '
    global current,target
    current = target = VM(p[3],[]) ; print 'new',target ; print VM.reg
def p_REPL_CMD(p):
    ' REPL : REPL CMD '
    assert target != None
    target.compile(p[2]) ; print target
def p_REPL_recur(p):
    ' REPL : REPL ex '
    print p[2]
def p_ex_SYM(p):
    ' ex : SYM '
    p[0] = p[1]
def p_REPL_COLON(p):
    ' REPL : REPL COLON SYM '
    target.V[p[3]] = target.Ip ; print target
def p_REPL_SEMICOLON(p):
    ' REPL : REPL SEMICOLON '
    target.compile('ret')
def p_REPL_BEGIN(p):
    ' REPL : REPL BEGIN '
    target.R.append(target.Ip) # mark current pos on return stack
def p_REPL_AGAIN(p):
    ' REPL : REPL AGAIN '
    target.compile(('jmp',target.R.pop()))  # compile jmp using R stack
                                                
def p_error(p): raise SyntaxError(p)
parser = yacc.yacc(debug=False,write_tables=False)  # create parser

parser.parse(open('src.src').read())                # run parser on src.src

print '======== exec ==========='
while not _bye: print current ; current.tick()      # run bytecode interpreter
