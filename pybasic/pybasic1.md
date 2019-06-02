# some key points in python

## print 
Print followed by multiple outputs, separated by commas  
`a=1`  
`print(a,type(a))`

## sequence
There are two kinds of sequences: tuple and list.

```
s1=(2,1.3,'love')
s2=[True,5,'smile']
print(s1,type(s1))
print(s2,type(s2))
```
## Index of elements
Subscripts for sequence elements start at 0  
`print(s1[0])`  
Basic Style [Lower Limit: Upper Limit: Step Size]  
`print(s1[2:0:-1])`  
(The Upper limit itself is not included.)

## Strings are tuples

## Operation
`print 'a' in ['a','b']`

## Indent
```
a=2  
b=1  
if a>b:
print a+b
else:
print a-b  
```
## Loop
range()  
for element in sequence  
while conditon:  
continue  
break  

## Function Define
```
a=1
def change_integer(a):
	a +=1
	return a

print change_integer(a)
print a

#===
b =[1,2,3]

def change_list(b):
	b[0] +=1
	return b
print change_list(b)
print b

```
  In the first example, we pass an integer variable to a function, which operates on it, but the original integer variable a does not change.
In the second example, we pass a table to a function, which operates, and the original table B changes.
For variables of basic data type, when variables are passed to the function, the function replicates a new variable in memory without affecting the original variable. (We call this value transfer)
But for a table, the table passes a pointer to the function, pointer points to the position of the sequence in memory, the operation of the table in the function will be carried out in the original memory, thus affecting the original variables. We call this pointer passing.

## Object-oriented programming
Python uses class and object to perform object-oriented programming (OOP) programming.
```
class Bird(object):
	have_feather= True
	way_of_reproduction = 'egg'
```
  References to *attributes* are implemented as objects.attribute,like 
```
summer = Bird()
summer.way_of_reproduction
```
## Object-objects programming 2nd
__init__() is a special method,Python has some special methods. Python treats them specially. The special method is characterized by two underscores before and after the name 
If you define the __init__() method in your class, Python will automatically call this method when you create the object. This process is also called initialization.
```
class happyBird(Bird):
   def __init__(self,more_words):
   print 'We are happy birds.',more_words 
   summer = happyBird('Happy,Happy!')
```

## dictionary
The elements of the dictionary are not in order. You cannot reference an element by subscript. The dictionary is referenced by a key.

```
dic = {'tom':11, 'sam':57,'lily':100}
print dic['sam']
```
## There are other ways to introduce in Python
```
import a as b
# import module a, and rename it as b
from a import function1 
# import function1 from module a, and it is not needed to explain the module when we use the objcet **function1**,**function1** is okay,not the**a.function1**.
from a import *
# import all the objects from module a.
```
## Search path
1. the folder wherer the program is located
2. standard library installation path
3. path included in the operating system environment variable PYTHONPATH  
If you have a custom module, or a downloaded module, you can place it in the appropriate path so that Python can find it.
```
import this_dir.module 
# a *__init__.py* must be in the directory *this_dir*,*__init__* can be an empty file.
```
## Exception handling
```
re = iter(range(5))
try:
	for i in range(100):
		   	print re.next()
except StopIteration:
	   	print 'here is end '
	   	print 'HaHaHaHa'
else:
		print 'go straight'
```
## Module using
```
from mod1 import function2

try:
	function2()
	function1()
except NameError:
	print 'NameError! Cannot use function1() without import it'
else:
   	print "Use function1() straightly" 

import mod1
print 'After import module mode1: '
mod1.function1()
```
