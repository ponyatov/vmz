import ply.lex  as lex
import ply.yacc as yacc

tokens = ['SYM','DIR']

t_ignore = ' \t\r'
t_ignore_COMMENT = r'\#.*'
def t_newline(t):
    r'\n'
    t.lexer.lineno += 1
    
def t_DIR(t):
    r'\.[a-zA-Z]+'
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
    
def p_error(p): raise BaseException(p)
yacc.yacc(debug=False,write_tables=False).parse(open('src.src').read())