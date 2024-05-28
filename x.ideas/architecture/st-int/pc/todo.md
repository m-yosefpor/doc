buffer channels in go -> add waitgroup



first struct, push and pop -> mutex -> hmm full,empty singal single channel in args -> then in struct -> run some time -> oh select, default to avoid deadlocks -> hmm missed singals and also two different lock -> I need to use condition var

then search condition variables ->
go in line func -> ooooh this bug is in v1.22
