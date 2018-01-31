#Write a function recurPower(base, exp) which computes base^expbase^exp by recursively calling itself to solve a smaller version of the same problem, 
#and then multiplying the result by base to solve the initial problem.

#This function should take in two values - base can be a float or an integer; exp will be an integer =0=0. 
#It should return one numerical value. Your code must be recursive - use of the ** operator or looping constructs is not allowed.
def recurPower(base, exp):

	if exp == 0:
		return 1
	else:
		return base*recurPower(base,exp-1)

#test case
res=recurPower(3,4)
print(res)