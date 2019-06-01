#!/usr/bin/env/python
#!/usr/local/bin/python

import pdb
class Bird(object):
	have_feather = True
	way_of_reproduction = 'egg'
	def move(self,dx,dy):
		position=[0,0]
		position[0]+=dx
		position[1]+=dy
		return position
	
class Chicken(Bird):
	way_of_move='walk'
	position_in_KFC=True

class Oriole(Bird):
	way_of_move='fly'
	position_in_KFC=False
	def move(self,dx,dy):
		position=[2,2]
		position[0]*=dx
		position[1]*=dy
		return position
	

class happyBird(Bird):
	def __init__(self,more_words):
		print 'We are happy birds.',more_words                            

class Human(object):
	def __init__(self,input_gender):
		self.gender=input_gender
	def printGender(self):
		print self.gender

summer_2 = happyBird('Happy,Happy!')
summer = Chicken()
summer_1 = Oriole()
print summer.way_of_reproduction
#pdb.set_trace()
print 'after move:',summer.move(5,8)

print summer_1.way_of_reproduction
#pdb.set_trace()
print 'after move:',summer_1.move(5,8)

Li_hua = Human('female')
print('{0} is {1}'.format('Li_hua',Li_hua.gender))
