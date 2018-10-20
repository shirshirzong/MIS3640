# prefixes = 'JKLMNOPQ'
# suffix = 'ack'
# for letter in prefixes:
#     if letter == 'O' or letter == 'Q':
#         print(letter + 'u' + suffix)
#     else:
#         print (letter + suffix)

'''index'''
# team = 'New England Patriots'
# letter = team[1]
# print (letter)

# print(team[0])
# # print(team[1.5]) string indices must be integers

# len(team)

# last = team[-1]
# print(last)


'''Traversal with a for loop'''
# index = 0
# while index < len(team):
#     letter = team[index]
#     print(letter)
#     index = index + 1

'''another way'''
# for letter in team:
#     print(letter)

'''string slices'''
team = 'New England Patriots'
# print(team[0:11])
# print(team[12:20])
'''omit the first or second index means starting from beginning or ending to the last'''
# print(team[:11])
# print(team[12:])


'''EXERCISE 5'''
str_1 = 'iPAD'
str_2 = 'Babson'
str_3 = 'python'


def any_lowercase1(s):
    for c in s:
        if c.islower():
            return True
        else:
            return False
print('1')
print(any_lowercase1(str_1))
# True or False?
print(any_lowercase1(str_2))
# True or False?
print(any_lowercase1(str_3))
# True or False?


def any_lowercase2(s):
    for c in s:
        if 'c'.islower():
            return 'True'
        else:
            return 'False'

print('2')
print(any_lowercase2(str_1))
# True or False?
print(any_lowercase2(str_2))
# True or False?
print(any_lowercase2(str_3))
# True or False?


def any_lowercase3(s):
    for c in s:
        flag = c.islower()
    return flag

print('3')
print(any_lowercase3(str_1))
# True or False?
print(any_lowercase3(str_2))
# True or False?
print(any_lowercase3(str_3))
# True or False?


def any_lowercase4(s):
    flag = False
    for c in s:
        flag = flag or c.islower()
    return flag

print('4')
print(any_lowercase4(str_1))
# True or False?
print(any_lowercase4(str_2))
# True or False?
print(any_lowercase4(str_3))
# True or False?


def any_lowercase5(s):
    for c in s:
        if not c.islower():
            return False
    return True

print('5')
print(any_lowercase5(str_1))
# True or False?
print(any_lowercase5(str_2))
# True or False?
print(any_lowercase5(str_3))
# True or False?
