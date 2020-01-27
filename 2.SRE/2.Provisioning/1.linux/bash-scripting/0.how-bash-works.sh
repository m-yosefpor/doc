man : manual
# whatis : short def (man -f)
whereis : dir of cmd
__

echo $arg1 $arg2 $arg3 ...  /	stdout: $arg1 $arg2 $arg3	/
cat $arg1 $arg2 $arg3 ... 	/	stdout: arg1+arg2+arg3		/ stdin: yes, but if stdin igonres other args 	/
---
pwd		/	stdout: working dir			/
cd	dir1	/	change directory to dir1 (if not default to ~), dir1 can be relative or absolute path
ls dir1 dir2 ...     / stdout: formatted names and infos of files in dir1 (if not , default `pwd`) and dir2 and ...

mkdir dir1/dir2 		/ dir 1 should exist 
rmdir



touch dir/file / dir should exist #also >a, but can't if needs sudo
				
				
				
				
				
				
				
				
				
############################################################
d : directory type file
a : any file
f : regular file


ad : file address (regular or dirctory) : aad, absolute : /d1/d2/d3/a
									      rad, relative : d1/d2/d3/a   # so `pwd`/relative is address
##########################################################

arg0 arg1 arg2 arg3 arg4 ### < in1  >in2 >>in3  ...  < > << >> & && | || * `` ''


0) search for < , > , >> , << , & , && , | , ||

for > (left to right) considers exact next arg and find file address ( if start with / absolute , if not relative) , if file exists clears that file, else touch it, and then  set it to be written by stdout, clearly the very left > will be the destination for stdout)
(remove all above from line)
## '>' is equivalent to '| tee' , but the key difference is that 'tee' can be used with 'sudo', but '>' is in user mode

1) searches arg0 in built-in 
	if find it then go to (3)
	esle to (2)
2) searches arg0 in $PATH
	if find it then to (3)
	else search repository
		if find : stderr? command 'arg0' not found, but can be installed with folan , return 1 2?
		else : command 'arg0' not found, did you mean folan , return 1 2?

3) give all other args to command


4) now the command search all args and considers args which starts with - :
	if -x exists ; set the option ; continue
	else : stderr? invalid option folan return 1 2; 
5) now hands the rest of args to comamand

6) command will do staff with input args and stdin, and may or may not stdout , stderr sth .

############################################################
cmd 1>a.txt 2>b.txt
