#Lesson 2: How to repeat (Procedures, Control)

print '''
Lesson 2: 
\t*How to repeat (Procedures, Control)
'''
page =('<div id="top_bin"><div id="top_content" class="width960">'
'<div class="udacity float-left"><a href="http://udacity.com">')
print page
start_link = page.find('<a href=')
print start_link

start_http = page.find('http:',start_link)
print start_http

stop_http = page.find(">",start_http)-1
print stop_http

url = page[start_http:stop_http]
print url 

#a procedure is initialized using the construct:
# def <name> (<parameters>): 
#	  <block>

'''
page = page[end_quote:]
start_link = page.find('<a href=')
start_quote = page.find('"', start_link)
end_quote=page.find('"', start_quote+1)


url=page[start_quote+1:end_quote]
print url

page = page[end_quote:]
'''

def rest_of_string(s):
	return s[1:]

print rest_of_string('audacity')


#sum procedure
''' here we take a and b and add them together and assign that value
to the variable a
'''
def sum(a,b):
	print "before the fxn is run, the value of 'a' is", a
	a = a + b
	print "after the fxn is run, the value of 'a' is", a
print sum (6, 6)


'''now we have added a return to the code'''
def sum(a, b):
	a = a+b
	return a

s = 'Hello '
t = 'Andrew!'
print sum(s, t)
#Note that when this runs, there is an error.
#print a


print '''
Define a procedure, square, that takes one number 
as its input, and returns the square of that 
number (result of multiplying
the number by itself).
'''

def square_a_num(num):
	num_squared = num * num
	return num_squared

print square_a_num(6)


'''
Define a procedure, find_second, that takes
two strings as its inputs: a search string
and a target string. It should return a
number that is the position of the second
occurrence of the target string in the
search string.
'''

def find_second(search_string, target_string):
	first_pos = search_string.find(target_string)
	second_pos = search_string.find(target_string, (first_pos+1))
	return second_pos
	
search = "she sells seashells by the seashore"
target = 'she'
print find_second(search, target)

#a better way to do this in one line would be as follows:
def find_second(search,target):
	return search.find(target, search.find(target)+1)
#what this does is it takes the string you are going to search and it passes it through
#then it says ok, I want to find the target string
#then it says BUT, I only want to find the target string after the first target is found

'''
Making Decisions
'''

#This code will take an input and return the absolute value of the input
def absolute(x):
	if x < 0:
		x = -x
	return x

print absolute(3)

#This code will take two numbers and return the bigger of the two
def bigger(num_1, num_2):
    if num_1 > num_2:
        return num_1
    else:
        return num_2

print bigger(1,2)

print '''
\t*Instructions
Define a procedure, is_friend, that
takes a string as its input, and
returns a Boolean indicating if
the input string is the name of
a friend. Assume I am friends with
everyone whose name starts with D
and no one else. You do not need to
check for the lower case 'd'

Second iteration we will be friends
with anyone whose name starts with 
D or N
'''

def is_friend(name):
	if name[0] == 'D' or name[0] == 'N':
		return True
	else:
		return False
	
print is_friend('Ned')


print '''
Define a procedure, biggest, that takes three
numbers as inputs and returns the largest of
those three numbers.
'''

def biggest(num_1, num_2, num_3):
	if (num_1 > num_2) and (num_1 > num_3):
		return num_1
	elif (num_2 > num_1) and (num_2 > num_3):
		return num_2
	elif (num_3 > num_1) and (num_3 > num_2):
		return num_3
	elif (num_1 == num_2) and (num_1 > num_3):
		return num_1
	elif (num_2 == num_3) and (num_2 > num_1):
		return num_2

print biggest(2,2,1)




























