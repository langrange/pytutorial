#!/usr/bin/env/python
#!/usr/local/bin/python
import sys

def isleapyear(year):
	if year % 4 == 0:
		if year % 100 != 0:
			print '{}'.format(year),'is a leap year.'
		elif year % 400 == 0:
			print '{}'.format(year),'is a leap year.'
		else:
			print '{}'.format(year),'is not a leap year.'
	else:
		print '{}'.format(year),'is not a leap year.'


year = int(sys.argv[1])
# print year
isleapyear(year)
