 #write a procedure, called biggest, which returns the key corresponding to the entry with the largest number of values associated with it. 
#If there is more than one such entry, return any one of the matching keys.
def biggest(dict):
   
    result = None
    big = 0
    for key in dict.keys():
        if len(dict[key]) >= big:
            result = key
            big = len(dict[key])
    return result
#test case
animals = { 'a': ['aardvark'], 'b': ['baboon'], 'c': ['coati']}

animals['d'] = ['donkey']
animals['d'].append('dog')
animals['d'].append('dingo')
print(biggest(animals))
