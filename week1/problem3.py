#Assume s is a string of lower case characters.

#Write a program that prints the longest substring of s in which the letters occur in alphabetical order. 
#For example, if s = 'azcbobobegghakl', then your program should print
s =input("Enter string of lower case characters :")
l= s[0]
curr= s[0]
for i in s[1:]:
    if i >= curr[-1]:
        curr += i
    else:
        if len(curr) > len(l):
            l = curr
        curr = i
print("Longest substring is" , l)