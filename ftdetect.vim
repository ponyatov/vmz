" assembly/compiler syntax for VM @ https://github.com/ponyatov/vm

" symlink this file into your ~/.vim/ftdetect/src.vim
" ln -fs ~/I/ftdetect.vim ~/.vim/ftdetect/src.vim

au BufRead,BufNewFile src.src set filetype=src
au BufRead,BufNewFile *.log set filetype=log|set autoread

au BufRead,BufNewFile *.ypp set filetype=yacc
au BufRead,BufNewFile *.lpp set filetype=lex
au BufRead,BufNewFile *.hpp set filetype=cpp
au BufRead,BufNewFile *.cpp set filetype=cpp
