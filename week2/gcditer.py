#Write an iterative function, gcdIter(a, b), that implements this idea. 
#One easy way to do this is to begin with a test value equal to the smaller of the two input arguments, 
#and iteratively reduce this test value by 1 until you either reach a case where the test divides both a and b without remainder, or you reach 1.

def gcdIter(a, b):
    
    c = min(a,b)
    
    while c > 0:
        if(a%c) == 0 and (b%c) == 0:
            return c
        else:
            c = c-1

#test case
res=gcdIter(6,9)
print(res)