#Assume that two variables, varA and varB, are assigned values, either numbers or strings.

#Write a piece of Python code that evaluates varA and varB, and then prints out one of the following messages:
#varA=input("Enter string1: ")
#varB=input("Enter string2: ")
#In this question we can't include input statements It should be automated.
if isinstance(varA, str) or isinstance(varB, str):
    print("string involved")
elif varA > varB:
    print("bigger")
elif varA < varB:
    print("smaller")
else:
    print("equal")