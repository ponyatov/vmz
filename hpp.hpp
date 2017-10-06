#ifndef _H_HPP
#define _H_HPP

								// opcodes
#define NOP 0x00
#define BYE 0xFF

#define Msz	0x100				// std.memory init size

#include <iostream>				// = std.includes
#include <iomanip>
#include <sstream>
#include <cstdlib>
#include <cassert>
#include <vector>				// variable size arrays
#include <map>					// symbol tables and registries
using namespace std;

struct VM {							// = virtual stack machine [wiki:VM]
	VM(string);						// constructor
	string dump();					// = dump VM state
	string head();					// short dump: name, sizes, state...
	// metainfo
	string name;					// VM name
	static map<string,VM*> reg;		// registry (all VMs must be here)
	static string reg_dump();		// dump registry
	// memory
	uint8_t M[Msz];					// main memory
	uint32_t Ip;					// instruction pointer (in place of PC)
	// compilation
	uint32_t Cp;					// compilation pointer
	void compile(uint8_t);			// compile bytecode command
	// bytecode commands
	void tick();					// execute one command:
	void nop();						// do nothing (filler in code)
	void bye();						// stop system
};

								// == lexer/parser interface [wiki:parser]
extern int yylex();				// = lexer (get next token)
extern int yylineno;			// current line number
extern char* yytext;			// lexed text
#define BC(OP)	{ yylval.cmd = OP; return CMD; }	/* ByteCode */
extern int yyparse();			// = syntax parser
extern void yyerror(string);	// syntax error callback
#include "ypp.tab.hpp"

extern void tick();				// do one command
extern VM* current;				// current VM will be used by bytecode executor
extern VM* target;				// target VM will be used by compiler

#endif // _H_HPP
