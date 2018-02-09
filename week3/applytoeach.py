#For each of the following questions (which you may assume is evaluated independently of the previous questions, 
#so that testList has the value indicated above), provide an expression using applyToEach, 
#so that after evaluation testList has the indicated value. 
#You may need to write a simple procedure in each question to help with this process.
def applyToEach(L, f):
    for i in range(len(L)):
        L[i] = f(L[i])
    return L
def addOne(s):
    return s + 1

def square(s):
	return s**2

def multiplyByFive(s):
	return s*5
#testcase
testList = [1, -4, 8, -9]
print(applyToEach(testList,square))
testList = [1, -4, 8, -9]
print(applyToEach(testList,addOne))
testList = [1, -4, 8, -9]
print(applyToEach(testList,multiplyByFive))
 	