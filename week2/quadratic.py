# Write a Python function, evalQuadratic(a, b, c, x), that returns the value
# of the quadratic a * x**2 + b * x + c.
#
# This function takes in four numbers and returns a single number.
def evalQuadratic(a, b, c, x):
    
    z = (a * (x**2) + (b * x) + c)
    return z
    
# Test case
testResult = evalQuadratic (2, 2, 3, 4)
print("The result is " + str(testResult))