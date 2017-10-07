" filetype detect for VM @ https://github.com/ponyatov/vm

" symlink this file: ln -fs ~/vm/ftdetect.vim ~/.vim/ftdetect/src.vim

au BufRead,BufNewFile src.src set filetype=src

au BufRead,BufNewFile *.log set filetype=log|set autoread
au BufRead,BufNewFile log.log set filetype=src|set autoread

au BufRead,BufNewFile *.ypp set filetype=yacc
au BufRead,BufNewFile *.lpp set filetype=lex
au BufRead,BufNewFile *.hpp set filetype=cpp
au BufRead,BufNewFile *.cpp set filetype=cpp
