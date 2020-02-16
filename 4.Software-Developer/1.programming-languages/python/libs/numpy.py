import numpy as np

### function or static method
### method

numpy.ndarray (objects M1)


ndarray have a dim, a (2,1) 2d array is not the same as (2,) 1d array and so on
so reshape all arrayes to (n,1) to be sure that they are 2Ds.

use len for 1d arrays


np.pi
---------
np.array( [1,2,3],[4,5,6], dtype=complex) # list, list of lists, list of tuples (but not tuples of sth)

np.zeros(t1)
np.ones(t1,dtype=np.int16)
np.empty(t1)
np.eye(n1)
np.arange(i1,i2,f1) # i1: begining, i2: end , f1: step
np.linspace(i1=0,i2,i3=1) # i1: beg, i2:end, i3:number of elements
np.random
	.random(t1)
	.uniform(f1,f2,t1)  # begining of interval, end of interval, size
	.normal(f1,f2,t1) # mean, standard dev, size
---
np.sin(M1)
np.sqrt(M1)
np.exp(M1)
np.abs(M1)
np.log(M1)
np.log10(M1)
---
np.dot(M1,M2)
np.matmul(M1,M2)

---
M1[i1]
M1[i1:i2]
M1[i1:i2:i3] # i2 step
M1[i1,i2] #if misses, then equal ':' 
M1[...,i1]
M1[...,i1,:]
M1[-1] #last
---
for o1 in M1
---
M1+M2 # element wise
M1-M2 # element wise
M1*M2 # element wise
M1**f1 # element wise
M1<f1 # M1 of bool
M1 @ M2 # matmul
---
M1.ndim # axes
M1.shape # tuple
M1.size # i
M1.itemsize
M1.dtype.name
--
M1.reshape(i1,i2)
M1.dot(M2)
M1.sum() # M1.sum(axis=0) M1.sum(axis=1) 
M1.min() #...
M1.max()
--
nd1.transpose()	


(static classes)


MATLAB??
--------------------------
puting two matrix side by side ( or chidan columns or rows)
copying some columns or rows, e.g. add [1;0] to every column 

