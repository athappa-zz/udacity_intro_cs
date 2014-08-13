#How to repeat


print '''
While loops
'''

i = 0 #initializes the variable i and sets it equal to 0

print '''example 1'''
while i < 10: #this tells python to keep iterating as long as i is less than 10
	print i #prints the iteration
	i = i + 1

print '''example 2'''
i = 0 #this tells python to set i equal to 0
while i != 10: #continues to run as long as i is not equal to 10
	i = i+1 #increments i by 1
	print i #prints out i to the interpreter


print '''
Define a procedure, print_numbers, that takes
as input a positive whole number, and prints 
out all the whole numbers from 1 to the input
number.'''

def print_numbers(input):
	i = 0
	while i < input:
		i = i + 1
		print i

print_numbers(2)

print '''
Define a procedure, factorial, that
takes one number as its input
and returns the factorial of
that number.
'''

print '''Option 1'''
def factorial(n):
	if n == 0: #splits code into 0, and everything greater than 0
		return 1 #0! is equal to 1
	else: #if you don't have 
		return n * factorial(n-1) #HOW DOES THIS "factorial(n-1) code work here??
		
print factorial(3)

print '''Option 2'''
def factorial(n):
	result = 1 #sets one variable to count and one for the ans. This is the ans.
	while n >= 1: #Iterate as long as n (the counter) is greater than 1
		result = result * n #take the result which is out of the loop and mult by n
		n = n - 1 #reduce the counter by 1
	return result

print factorial(4)




#break statement example
print '''
using the break statement
'''
for n in range(2, 10):
	for x in range(2,n):
		if n % x == 0:
			print n, 'equals', x, '*', n/x
			break
	else:
		print n, 'is a prime number'


print '''
append'''

list1 = [1,2,3,4,5,6,7]
list2 = [8,9,10]

for i in list2:
	list1.append(i)

print list1


print '''
'unlist' a list within a list'''

list1 = [["Andrew", "Clay", "Cameron"], [1,2,3,4,5], ["Mexico", "Bahrain", "Djbouti"]]

for i in list1:
	for x in i:
		print x

for i in range(10,0,-1):
	print i






































