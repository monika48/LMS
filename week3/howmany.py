#write a procedure, called how_many, which returns the sum of the number of values associated with a dictionary
def how_many(dic):
    
    count = 0
    for l in dic.values():
       for i in l: count += 1
    return count

#testcase
animals = { 'a': ['aardvark'], 'b': ['baboon'], 'c': ['coati']}

animals['d'] = ['donkey']
animals['d'].append('dog')
animals['d'].append('dingo')
print("number of entries in given dictionary:",how_many(animals))