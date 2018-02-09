'''
Write a procedure called oddTuples, which takes a tuple as input, and returns a new tuple as output, 
where every other element of the input tuple is copied, starting with the first one. 
So if test is the tuple ('I', 'am', 'a', 'test', 'tuple'), then evaluating oddTuples on this input would return the tuple ('I', 'a', 'tuple').
'''

def oddTuples(aTup):
    i = 0
    newTup = ()
    for index in aTup:
        if i%2 == 0:
            newTup += (index,)
        i += 1
    return newTup

#Test Code
print(oddTuples((1, 2, 3, 4, 5)))


print(oddTuples((1,2,3,4,5,6,7,8,9)))