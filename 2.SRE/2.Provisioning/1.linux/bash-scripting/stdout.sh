echo hi == echo 'hi'  # get a str and put it to stdout (not a file name or sth)
cat hi == cat 'hi' # get a file name and output that to stdout

cmnd1 | cmnd2 # exec cmd1 and put the output to stdout and gives it as stdin to cmnd2

cmnd1 > hi # exec cmd1 and put the stdout and writes to a file with name hi
cmnd1 >> hi # same as above, but append


cmnd1 | tee hi # tee gets the output and writes it both to file hi and also to stdout

cmnd1 | tee hi >/dev/null  #only output to hi

cmnd1 | tee -a hi >/dev/null #same above but append



** the only advantage of '| tee hi >/dev/null'   to   '>hi' is that it could be used with sudo.. so 
sudo echo hi > /bin/bash #permission error #only run echo as sudo not redirection

echo hi | sudo tee /bin/bash >/dev/null # no error
