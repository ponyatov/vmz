" assembly/compiler syntax for VM @ https://github.com/ponyatov/vm

" symlink this file: ln -fs ~/vm/syntax.vim ~/.vim/syntax/src.vim

syntax match Comment	"\v#.*$"			
syntax match Special	"\v\.[A-Za-z]+"		" directive 
syntax match Keyword	"\v(nop|bye)"		" machine opcodes
syntax match Special	"\v(vm|M|Ip|Cp):"
