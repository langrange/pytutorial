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
```
print f(1,c=3,b=2)		
# Note: *But the positional parameter will appear before the keyword argument*		
```		
