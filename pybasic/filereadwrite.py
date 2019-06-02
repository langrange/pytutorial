#!/usr/bin/env/python
#!/usr/local/bin/python

f=open('record.txt','r')
content = f.readlines()

for item in content:
	print item

f.close()
