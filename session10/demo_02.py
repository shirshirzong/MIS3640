'''MAP -- applies to a function to all the items in an input_list'''

t = ['a','b','C']
def capitalize_all(t):
    res = []
    for s in t:
        res.append(s.capitalize())
    return res

print(capitalize_all(t))


'''REDUCE -- that combines a sequence of elements into a single value'''
t = [1,2,3]
print(sum(t))


'''select some of the elements from a list and return a sublist'''
def only_upper(t):
    res = []
    for s in t:
        if s.isupper(): #if this .isupper function works
            res.append(s)
    return res
    pass


'''DELETING ELEMENTS'''
t = ['a', 'b', 'c', 'd']
x = t.pop(1)
# pop modifies the list and returns the element that was removed. 
print(x)
print(t)

x = t.pop()
# If you don’t provide an index, 
# it deletes and returns the last element.
print(x)
print(t)


t = ['a', 'b', 'c', 'd', 'e']
del t[1:3]
#from index one, until/before index 3
print(t)

t = ['a', 'b', 'c']
t.remove('b')
print(t)

'''to convert a string into a list of characters (list is a inbuilt function'''
team = 'Patriots'
t = list(team)
print(t)

s = 'spam-spam-spam'
delimiter = '-'
# delimiter = 'm'
t = s.split(delimiter)
print(t)

t = ['New', 'England', 'Patriots']
team = ' '.join(t)
print(team)


a = [1, 2, 3]
b = a
#If a refers to an object and you assign b = a, then both variables refer to the same object:
b is a
b[0] = 'something else'
print(a)

'''to sort/modify a list, but also wanna keep the original, just create a copy'''
t = [3, 1, 2]
t2 = t[:]
t2.sort()
print(t)
print(t2)