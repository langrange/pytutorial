dic = {'tom':11, 'sam':57,'lily':100}

print('Before change, sam is {}'.format(dic['sam']))
dic['sam']=60
print('After change, sam is {}'.format(dic['sam']))

for key in dic:
	print('{} is {}'.format(key,dic[key]))

del dic['lily']
print(dic.items())
