#Given a variable x, that stores the value of any decimal
#number, write Python code that prints out the nearest whole
#number to x. If X is exactly half way between two whole numbers
#round up so 3.5 rounds to 4 and 2.5 rounds to 3. Assume x
#is not negative.


x = 27.63
print x

dec = str(x).find(".")
print dec

left_of_dec = str(x)[0:dec]
print left_of_dec

right_of_dec = str(x)[(dec+1):]
print right_of_dec

if int(right_of_dec[0:2]) < 50:
	print left_of_dec
else:
	print int(left_of_dec) + 1