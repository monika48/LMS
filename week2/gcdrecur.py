#Write a function gcdRecur(a, b) that implements this idea recursively. 
#This function takes in two positive integers and returns one integer.
def gcdRecur(a, b):
	while a!=b:
		if a>b:
			return gcdRecur(a-b,b)
		else :
			return gcdRecur(a,b-a)
	return a
#test case
a=int(input("Enter no 1:" ))
b=int(input("Enter no 2:" ))
res=gcdRecur(a,b)
print("GCD is: ",res)