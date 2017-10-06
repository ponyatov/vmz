log.log: src.src ./exe.exe
	./exe.exe < $< > $@ && tail $(TAIL) $@
C = cpp.cpp
H = hpp.hpp
./exe.exe: $(C) $(H)
	$(CXX) $(CXFLAGS) -o $@ $(C)
