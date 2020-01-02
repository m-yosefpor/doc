when we call a Object, it returns a copy of itself, but without callable or what??


objects:
module
type ## o1.__class__ = object type of the class
    #this is a special type, alot of later methods doesn't work for this kind of objects
--
bool
int
float
complex
str
list
tuple
dict
set
range
--
user defined objs
--
function
builtin_function_or_method
--

is
############################################################
#defining objects:

name1 = o1 #make a copy of obj with name name1

import module1 (as module2) #make a new object module base on the specific file/folder in the directory and names it as module1 (or module2 if specified)
from some.path.to.module import module1/class1 (as name1) #again creat a module/type object with the corresponding name






#defining new attribs for objects(EVERY obj, even moduls.. we can insert a type obj there :) :
o1.a1 = 2  #set a new/overwirte attrib for o1  # o1 can't be built in objects, or even objects with __class__ of a built in object , except for user defined classes that work , althogh their type is type??/
o1.a1.a2.a3 = 4 # eval o1.a1.a2 obj and set attrib a3 for that
o1.__class__.a1 =2 # so this change the a1 of every instance of the class

o1.a1 : #if a1 in o1 attribs then return that obj, else return o1.__class__.a1 (when o1.__class__ is 'type' then error : object has no attribute a1

o1.__class__ = cl2 #then all attribes and methods of that included

# or in __init__(self): self.__class__ = cl1

if type(o1) == type: o1() , when called, then an instance is created such that it doesnt have the atribs of __init__ , but it can be used with __addr__ and __len__ and othe built ins.. note that all oher attribs (methods only), will be called with self=o1() .. esp __init__

creating new objects




##########################3
getattr(o1,s1) : s1 name of attrib
setattr(o1,s1,o2)
