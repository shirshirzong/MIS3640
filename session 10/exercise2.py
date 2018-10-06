t = ['a', 'b', 'c', 'd']

#list.append(x): add an item to the end of the list, same list
t.append('apple')
print(t)

#extend(iterable):taking each element in the iterable and append to end of list
t.extend('banana')
print(t)

#insert(i,x) i - index, given positiom, x - value to be inserted
t.insert(2, 'after b')
print(t)

#remove(x) x must be the first item in the list
t.remove('a')
print(t)

#pop(i): remove item from given position, if not specified, removes the last item
t.pop(1)
print(t)
t.pop()
print(t)

#clear(): remove all the items from the list == del [a:]
# t.clear()
# print(t)


#index(x): return index in the list of the first item whose value is equal to x
print(t.index('apple'))
print(t.index('b'))
#there are 2 'b's but return the first one's index

#count(x):return the number of times value x appear in the list
print(t.count('b'))
print(t.count('a'))

#sort():sort items in order / use sorted(list). sorted does not change the orignal list, .sort does
t.sort()
print(t)
# print(sorted(t))
# print(t)

#reverse()
# t.reverse()
# print(t)

#copy()
print(t.copy())