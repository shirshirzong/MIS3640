'''Exercise 3'''
team = 'Babo boo hoo'

print(team.split(' '))
print(team.split('b'))
print(team.strip())
print('www.example.com'.strip('cmowz.')) #why there is z in here
print('Funawish'.strip('wanu')) #why this one doesnt work
print(team.replace('hoo','meh'))
print(team.replace(' ','+'))


'''Exercise 4_1'''

def price(x):
    count = 0
    for letter in x:
        count += ord(letter) - 96
    return count

print('bananas ', '$',price('bananas'))
print('rice ', '$', price('rice'))
print('paprika ', '$', price('paprika'))
print('potato chips ', '$', price('potato chips'))
print('-------------------------') # 25
print('Total ', '$', price('bananas')+price('rice')+price('paprika')+price('potato chips'))


'''Exercise 4_2'''

print('{:18} {:1} {:6}'.format('bananas', '$', '52.00'))
print('{:18} {:1} {:6}'.format('rice', '$', '35.00'))
print('{:18} {:1} {:6}'.format('paprika', '$', '72.00'))
print('{:18} {:1} {:6}'.format('potato chips', '$', '78.00'))
print('--------------------------') # 26
print('{:17} {:1} {:6}'.format('Total', '$', '237.00'))



'''Exercise 4_3'''

print('{:14} {:1} {:6}'.format('bananas', '$', '52.00'))
print('{:14} {:1} {:6}'.format('rice', '$', '35.00'))
print('{:14} {:1} {:6}'.format('paprika', '$', '72.00'))
print('----------------------') # 22
print('{:13} {:1} {:6}'.format('Total', '$', '237.00'))