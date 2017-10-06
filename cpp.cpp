#include "hpp.hpp"

#define YYERR "\n\n"<<yylineno<<':'<<msg<<"["<<yytext<<"]\n\n"
void yyerror(string msg) { cout<<YYERR; cerr<<YYERR; exit(-1); }

int main() {
	yyparse();					// run assembler/compiler
	for (;;) current->tick();	// infty execution loop
}

VM::VM(string N) {
	name = N;								// set VM name
	Ip = 0;									// reset instruction pointer
	Cp = 0;									// reset compilation pointer
	reg[N]=this;							// register new VM
}

string VM::head() { return "vm:"+name; }
string VM::dump() { string S = head(); return S; }

map<string,VM*> VM::reg;
string VM::reg_dump() { string S = "VM list:";			// dump VM_reg
	for (auto vm=reg.begin(),e=reg.end();vm!=e;vm++)	// for over registry
		S += '\n'+vm->second->head();
	return S; }

void VM::compile(uint8_t C) { M[Cp++]=C; assert(Cp<Msz); }	// compile byte

VM* current=NULL;		// current VM will be used by bytecode executor

void VM::tick() {
	assert( Ip < Cp );					// check Ip in code < compile point
	uint8_t cmd = M[Ip++];				// = FETCH command opcode
	switch (cmd) {									// = DECODE/EXECUTE
		case NOP: nop(); break;
		case BYE: bye(); break;
		default:									// unknown command
			ostringstream os; os << "bad opcode: "
				<< "vm:" << name << ' '
				<< hex << setfill('0') 
				<< setw(4) << Ip-1 << ':'
				<< setw(2) << (int)cmd << ' ';
			yyerror(os.str());
	}
}

void VM::nop() {}
void VM::bye() { exit(0); }

