AFC_east = ['New England Patriots', 'Buffalo Bills', 'Miami Dolphins', 'New York Jets']
numbers = [42, 123]
empty = []
# print(AFC_east, numbers, empty)
# print(numbers[1])

AFC_east[3] = 'New York Giants'
# print(AFC_east)

AFC_east = ['New England Patriots', 'Buffalo Bills', 'Miami Dolphins', 'New York Jets']
# print('Buffalo' in AFC_east)


'''Exercise 1'''
L = [
    ['Apple', 'Google', 'Microsoft'],
    ['Java', 'Python', ['Ruby','On Rail'], 'PHP'],
    ['Adam', 'Bart', 'Lisa']    
]
# Index of 'Apple'
print(L[0][0])

# Index of 'Lisa'
print(L[2][2])

# Index of 'On Rail'
print(L[1][2][1])


'''Traversing A list'''
numbers = [2, 0, 1, 6, 9]

for i in range(len(numbers)):
    numbers[i] = numbers[i] * 2
    
print(numbers)

'''Exercise 2 play around'''



'''List Slices'''
t = ['a','b','c','d','e','f']

print(t[1:3])
