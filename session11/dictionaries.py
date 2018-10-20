# names = ['Defne', 'Jack', 'Angela']
# scores = [95, 75, 85]

# grades = dict()
# print(grades)
# # {}


# grades['Defne'] = 90
# print(grades)
# # {'Defne': 90}

# grades ={'Defne': 90, 'Jack': 75, 'Angela': 85}
# print(grades)

# # {'Defne': 90, 'Jack': 75, 'Angela': 85}

# print(grades['Jack'])
# # 75

# print(len(grades))
# 3

# def histogram(s):
#     d = dict()
#     for c in s:
#         if c not in d:
#             d[c] = 1
#         else:
#             d[c] += 1
#     return d

# h = histogram('Bookkeeper')
# print(h)
# {'B': 1, 'o': 2, 'k': 2, 'e': 3, 'p': 1, 'r': 1}

# number_of_e = h.get('e')
# number_of_a = h.get('a')
# print(number_of_e)
# print(number_of_a)

'''Exercise 1'''
# def histogram(s):
#         d = dict()
#         for c in s:
#                 d[c] = d.get(c,0) + 1
#         return d

# h = histogram('Bookkeeper')
# print(h)



'''Looping and dictionaries'''
# def print_hist(h):
#         for c in h:
#                 print(c,h[c])

# h = histogram('Massachusetts')
# print_hist(h)