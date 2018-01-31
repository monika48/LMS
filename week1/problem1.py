#Assume s is a string of lower case characters.

#Write a program that counts up the number of vowels contained in the string s. Valid vowels are: 'a', 'e', 'i', 'o', and 'u'. For example, if s = 'azcbobobegghakl', your program should print:
string=input("Enter string:")
vowels=0
for i in string:
           if(i=='a' or i=='e' or i=='i' or i=='o' or i=='u'):
                vowels=vowels+1
print('number of vowels is:',vowels)