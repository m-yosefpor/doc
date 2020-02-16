############################################################
'''
intro
'''
############################################################
import time
t0=time.time()
#####
import sys,contextlib,os
#####
import multiprocessing as mp
import numpy as np
import pandas as pd
import sympy as sym
import scipy as sp
import matplotlib.pyplot as plt
#import sklearn as sk
#import tensorflow as tf
#####
print('import time : {:.2f}'.format(time.time()-t0))
############################################################
1) all imports at the begining
instead of from sth import a , use import sth
and use sth.a
this is more generalizable and readable and pythonic # but import time, interpretation time??


2) functions next: use functions as frequent as possible

def my_function'always use my_ at first' (N = 20 #always default value even None, except esp cases which want to raise error):
        '''
        N : int : number of samples : O(N)
        n_jobs : int : sth : O(1)

        --- return ---
        data : pd.DataFrame : data
        '''
        a=2
        return data


3) main
#when calling function always call with key, except for verrrrry famous ones
#when calling them with key, use variables outside calling for chaning ones, use the exact same name


#when calling an object from a class, use exact class name with a number:
RandomForestClassifier_1 = RandomForestClassifier()
always use methds instead of functions, if possible: sym.diff(f,x,2) # f.diff(x,2)

############################################################
to do for programming readability

variable names:
	meaningful, complete, with underline,
#?	type of them (i,b,f,c, s,l,t,set,d , df , nd ,)

for big numbers:
    use _ for readablity like 30_000
    use e for bigger ones 1e6 # note that it's float and different from 1_000_000

use reshape for nd arrays always

NO numbers... all numbers parametrize and in a place moshakhas

use %%time in jupyter or t0(begining), t1,t2 (interval) , time.time()-t0 for end

###########

