#!/usr/bin/env/python
#!/usr/local/bin/python

a=2
b=1
if a>b:
   print a+b
else: 
   print a-b

print('{0},{1}'.format('zhangk', 32))
 
print('{},{},{}'.format('zhangk','boy',32))

print'I am','{}'.format('zhangk','boy',32)
 
print('{name},{sex},{age}'.format(age=32,sex='male',name='zhangk'))
 
print('{:>8}'.format('zhang'))
print('{:0>8}'.format('zhang'))
print('{:a<8}'.format('zhang'))
print('{:p^10}'.format('zhang'))
 
print('{:.2f}'.format(31.31412))
 
print('{:b}'.format(15))
 
print('{:d}'.format(15))
 
print('{:o}'.format(15))
 
print('{:x}'.format(15))
 
print('{:,}'.format(123456789))
