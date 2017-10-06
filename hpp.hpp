#ifndef _H_HPP
#define _H_HPP

#include <iostream>				// = std.includes
#include <cstdlib>
using namespace std;

struct VM {						// = virtual stack machine [wiki:VM]
};

								// == lexer/parser interface [wiki:parser]
extern int yylex();				// = lexer (get next token)
extern int yylineno;			// current line number
extern char* yytext;			// lexed text
extern int yyparse();			// = syntax parser
extern void yyerror(string);	// syntax error callback

#endif // _H_HPP
