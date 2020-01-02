#! /usr/bin/python3


#after colon it's ok to write statement1 if only one
#can use any spacing for block
#can use ; in ending or not #useful when more than a command in a line
-----------------------
#cmd commands
python --version
python a.py
python -m pip install --upgrade pip
python -m venv sth
---
python file.py < input.txt >output.txt # my pc doesnt make pyc :/ slower?
file.py
--
python #runs IPython
----------------------------
#package:(type module) contains lots of modules. (type say it is a module but its not, it can be used with package.module, packages are folders of modules
import package # import whole modules in package, must be accessed via name: package.package.module.class??
import package.module ## must access via package.module.class
from package import module (as newname) #then  classes in module can be access via module.class
from package.module import class
import package.module.class !error

----------------------------
#every modul contains (classes(types) , functions, variable) (i.e. objects of type 'type' or else.. all are attribes) , its actuall a .py file
import module (as newname)
from module import function/class (as newname)
import module.class !error (cause module.class is not a modul to be imported
----------------------------
class sdf:
    '''
    class description goes her
    '''
    variables (every object)
    ### attribs can be added later in the object!! o1=c1() o1.a=2
    ### since classes are objects, then static vars are like object vars no difference
    ### so then every object of a class can have different attribs .. only methods are the same!
    ### methods are also attribs of class obj!! don't call them and you can change them or even define them layer using class.fun = sth .. note : not : class.fun()
    ## cool like dicts.. but have 1.constructor 3.make instances and copies 3.self 4.staticmethod

    def __init__(self,a,b): #constructor
        instance_variable = 2
        self.globalvar(in all class) = 3 # no need for pre defined ,can defiend first in any method

    def method (self,function objects):
        '''
        every method description comes here and appears in help()
        '''
        print('hi') # no return statement is same as return with no argument

    @staticmethod
    def method(a,b): # no self required
        print('hi static')


class subcla(sdf):
    def __init__(self):
        super(subcla,self).__init__()
        self.a=2
    def method(self): #overwirte methods by using the same names
        return
################
#generic
#overloading
## methods which change the objects


????????? function decoration with @
operator making
indexing making
iter ?
-------------------------------------
    decimal #fixed precesion
	fraction
    dict_keys
	file (file) #_io.TextIOWrapper 
	__main__.abc #user defined classe abc
-----------------------------------------
#especial characters #even in strings
{}
''
[] #list or indexing both
() , tuple , call , making priority, ...
; 
:
. 
,
% #?
# #?
"""multiline str"""
'''also'''
--------------------------------------------
#other reserved words
and or not is
lambda
def , class
----------------------------------------------
f0 == i0 # True!
----------------------------------------------
if b1:
	sth1
	sth2
elif b2:
	sth3
	sth4
else:
	sth5
	sth6
---
o1 in o2 #return bool, o2 must be iteratalbe
----
for o1 in o2:
	sth1
	sth2
    continue
    break

for o1 in o2 : sth1

sth1 for o1 in o2 # use in [] or {} for init

while True:
    pass

--- 
try:
	sth1
	sth2
except:

else:

finally:
---
del o1
--
pass


isinstance
locals
globals
**************************************************
##class
#classes are objects of class type.. and so class type is in turn an object of class type :) :?
	#add 1 for objects
----
#this classes __init__ made such that , when class(o1) then o1.__class__() will be given if not the specified type  , so new classes could be written such that we def a built in method for their constructor
#(casting) ## MUST return a valid data type (or at least castable??) , but can do anything in them
-----
type #even types are objects :/
		#returns the class name of object
        #returns <class 'type'> if a class
		#'class' type is 'type', class of a class not an obj
	
-----
bool(b) ## __bool__
int(i) ## __int__
float(f) ##__float__
complex(c) ##__complex__
--
str(s)  ##__str__

## must be iteratable
tuple(t)
list(l)
set(set)
dict(d)

range(r) #in python2 where list, but a new datatype in py3
slice

**************************************************
##object
True
False
---
0 1 2 3 4 5 6 7 8 9 , # and all other numbers
1_23
1e4
1e-4
1.24
.234
### important note here is that 0.1 doesn't envoke method 1 of 0, '.' only invokes method if object name AND method name is not started with a number i.e.: a=0 b=1 then a.b is syntax error
**************************************************
##builtin_function_or_method 
# can do anything in this methods , even printing or whatever, but ONLY REMEMBER return type shoud be exactly the same ( e.g. for int , shoud return an int )
# there is a default for every class even if you not defined
# fun() is equal to a.__fun()__
-
dir() # __dir__ : return 'list' of all methods(built in and other) of an obj
len() # __len__ # return type MUST be int?
repr() # __repr__
abs() # __abs__ not for list,tuple ,... #return type can be any?
iter() # __iter__
---
class PrintNumber:
    def __init__(self, max):
        self.max = max

    def __iter__(self):
        self.num = 0
        return self

    def __next__(self):
        if(self.num >= self.max):
            raise StopIteration
        self.num += 1
        return self.num


-----
#must be iteratable
max , min , sum

any # returns True if any of the iteratble objects be True, and else False
all # returns True if all of the iteratble objects be True, and else False
-----
(general functions)

print(o1) #print str(o1)
input(o1) #print str(o1) and inputs sth, return str
help(o1) ## read comments in defining a class and making sth cool
---
(some type specific functions)

pow,  round, hex, bin
open(file)
ord(s1) #len(s1) must be 1 #return unicode
***************************************************
##operators
#space is important in here : + = error or even = = 
	+ - * / ** // % ~ & |
	== != < >
	= += -= *= /= %=
	not or and

#a <opr> b :: a.__oprname__(b)
a + b : a.__add__(b) b.__radd__(a) #radd if add fails
a - b : a.__sub__(b) b.__rsub__(a)
a * b : a.__mul__(b)
a / b : a.__div__(b)
a ** b ,also pow(a,b): __pow__
---
def __iadd__(self, other):
    self.cart.append(other)
    return self #if return anything else, will substitue it, if not type would become None

+= __iadd__
-= __isub__
*= __imul__
/= __idiv__
-----
== __eq__
!= __ne__


----
a[o1] : a.__getitem__(o1) ??slice works but how?
a[o1] = 2 : a.__setitem__(key:value)??
---
#https://realpython.com/operator-function-overloading/

*************************************************
**************************************************
**************************************************
##bool
b1 = True
b2 = False
**************************************************
##int
i0 = 0
i1 = 2

----cast---
b #if 0 is False else is 1
i
f #add .0
c
--
s
**************************************************
##float
f0 = 0.0
f1 = 2.0
f2 = 3.4
----cast---
b
i #float(truncate)
f
c
s
**************************************************
##complex
c0 = 0j
c1=1+0j
c2 = 1.1 + 2.3j
**************************************************
#### indice operator : list, str, tuple
# __index__ method
# b1 auto cast to i1, but not f1 or c1
l1[n1] #return o1 in n-th index  0<= n <= N-1 ,,  - (N-1) <= n <= -1 :: map :: 0 <= n <= N-1
      #if not in the range, list  index out of range


l1[n1:n2] # return l2 , first map in n negative, then : indexes map(n1), map(n1)+1 ,... ,map(n2)-1
    #if map(n1) >= map(n2) returns []
l1[n1:n2:n3] #n3 is step size != 0
    #maps n1 and n2
        #if n3 >0 :if map(n1)>= map(n2) [] else starts from map(n1) , add n3 to reach map(n2), excluding itslef
    #if n3 <0 : if map(n1) <= map(n2) [] else then starts from map(n1), add n3, to reach map(n2) excluding itself
    # if n1 ro n2 not specified: continues to reach one of the ends of array

l1[3:2] # []
l1[3:3] # []

l1[:n] 
l1[n:]
l1[:] #high level copy
l1[-1] # last element
l1[-3:] # last 3 elements

l1[::-1] # reverse
l1[::2] # yek dar mion
*************
#np.arrays are even cooler:
    l [l1] #l1 np array auto cast to list
    l1 can a be a list of any int, even repetative, however map(n1) should be in range

    if bool: not autocast, but as a mask, but should be the same as len(l)
    this is really cool like l[l1!=3]

**************************************************
##str
#immutable , ordered , iteratable
#made from chars not objects, and is not a list
s0=''
s1 = 'abcd'
s2 = r'akdjfka\n dkfa\f ' #changes all \ to \\
# u'adkfja' is equal to 'adsfa' in py3, since all strings are unicode by default in py3
s3=b'ajafkjdaf' #binary
---
S1 + S2
S1 * n1
s1 += s2
s1 *= n1
---
str(o1) #o1:  #is this toString method?

# old formatting: '%s aslfsja f%s' %('he', 'sf')
'{0} afasf {1}'.format('smat','sdf')
'{} asdf {}'.format('hi','hello')
#https://pyformat.info/
---

s1.index(s2) 
s1.find(s2) #returns -1 if not found, but index throws an exception
s1.replace(s2,s3) #s1.replace(s2,'') delete s2
s1.split(s2) #return list #s2 not contained
s1.splitlines() #for multi line strings
s1.upper()
s1.lower()
s1.isalpha() # return bool
s1.isdigit() # return bool
s1.strip() 
s1.rstrip() # removes right whitespaces and \n

s1.encode() # 's1' to b's1'
s1.decode() # b's1' to 's1'

**************************************************
##tuple
#immutable , ordered , iteratable
t1 = (o1,o2,o3, ...)
t1 = o1,o2,o3
tuple(o1)
t1 = () #empty tuple
t1 = (o1,) #t1=(o1) type(o1) = o1
--
t1[n1]
--
t1.index(o1)
t1.count(o1)
--
len(t1)
---
t1+t2

**************************************************
##list
#mutable, ordered, iteratable
l0=[] #empty list
l1 = [o1,o2,o3,...]
list(o1) # o1: tuple,str, list
---
--
l1 + l2
l1 * n1
l1 += l2
l1 *= n1
--
l1.append(o1) #$$ o1 : None # l1 +=[o1]
l1.insert(n,o1) #$$ o1 : None  #such that o1 ind becomes n, shift n and other to right
l1.remove(o1) #$$ o1 : None
l1.pop(n) #$$ n1 : o1 #pops n index 
l1.clear() #$$ None:None
l1.reserve() #$$ None:None #l1[::-1] doesn't change
l1.sort() #$$ None:None

l1.index (o1)
l1.count(o1)
l1.copy() # None : list # l1[:]
---
del l1[n]
---
casting
len , min , max , sum

**************************************************
##set
#unordered , mutable, iteratable
set1={a,b,c}
set1 = {} #empty set
set(o1) # o1 : str , list, tuple , 
---
set1[o1]
--
 set1.add(o1)
 set1.update([o1,o2,o3])
 set1.remove
 discard
 pop
 clear

--

set1 & set2
set1 | set2
set1 - set2

--
casting
len, min , max , sum
**************************************************
##dict
#mutable , unordered
# dict keys must be immutable
d={
	o1:o2,
	o3:o4,
	o5,o6
}
dict(o1) #o1 :

--
len(d1)
--
o1 in d1 #return bool
--------------------------------------------
--------------------------------------------
##file
file1 = open('dir','attrib') # r a w x , t b #default rt
--
file1.read()
file1.read(n1)
file1.readline()
file1.write(s1)
file1.close()
--
for x in file1 #line by line
--------------------------------------------
##function
fun1 = lambda o1 , o2 , ... : o3
--------------------------------------------
##module
--------------------------------------------
# some useful tips
list(map(int,l1)) # changing a list of string to list of int
list(set(l1)) # remove repetitive
int(f1) # cut off
len(str(o1)) # for number of digits

 a > b ? f : g
 (g,f)[a>b]

nd1[::-1] # reverse
list(enumerate( l1 , n))
