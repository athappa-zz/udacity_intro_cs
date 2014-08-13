#Loop examples

from sys import argv #import command for argument variable

print '''
example 1
'''
script, username = argv #here we use argv to get the program/user name

#in order to run this properly, you need to type "python loops_2.py andrew"

print "Hey, welcome to the %s program, %s" % (script, username)
print "I'm going to ask you about all the places you've visited"
print "Before starting, please enter the number of places you want to discuss"
number = int(raw_input("> ")) #user inputted number which we will use later in the loop
print "Thank you!"
print "Now, where have you traveled to?"
places_traveled = [] #this is an empty list (container) to hold entered values

for i in range(number): 
	places = raw_input("*** ") #the raw inputs will show whatever chars are in the ""
	places_traveled.append(places) #for i through n places, they will be appended
								   #to places_traveled

print "Here's a list of places you've been to \n", places_traveled #\n is a newline char

print '''
example 2: prime numbers
'''

for i in range (2,20): #this is used to get numbers ranging from 2 to less than 20
	for x in range (2,i):
		if i % x == 0:
			print i, "equals", x, "*", i/x
			break
	else:
		print i, "is a prime number"

print '''
multiple assignment
'''

s='andrew'
t='thappa'

s, t = t, s

print s
print t