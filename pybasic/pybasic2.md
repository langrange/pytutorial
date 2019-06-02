## Function parameter passing
### position passing
```
def f(a,b,c):
	return a+b+c
print f(1,2,3)			
```
### keyword passing
```
def f(a,b,c):
	return a+b+c
print f(c=3,b=2,a=1)			
```
Keyword delivery can be mixed with location delivery  
*But the positional parameter will appear before the keyword argument*		
```
print f(1,c=3,b=2)		
```		
### default value of parameter
**Note:** this defualt value must be at the last, it means that  
non-default params should all be before than default params.
```
def f(a,b,c=10):
	return a+b+c

print f(3,2)
print f(3,2,1)
```
### packing passing
When defining a function, we sometimes don't know how many parameters are passed when the call is made. At this time, it is useful to pack the positional parameters, or to wrap the keyword parameters for parameter passing.
 packing position passing  
```
def func(*name):
	print type(name)
	print name
func(1,4,6)
func(5,6,7,1,2,3)
```
 packing keyword passing
```
def func(**dict):
	print type(dict)
	print dict 
func(a=1,b=9)
func(m=2,n=1,c=11)
```
### unpacking passing
 unpacking tuple
```
def func(a,b,c):
	print a,b,c
arg = (1,3,4)
func(*args)
```
 unpacking dictionary
```
dict = {'a':1,'b':2,'c':3}
func(**dict)
```
### mixed
**order:** position passing --> keyword passing --> packing position --> packing keyword passing
