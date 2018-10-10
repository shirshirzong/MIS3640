def print_lyrics():
    print("what's up fam")
    print("nothing much")

type(print_lyrics)
print_lyrics()

def repeat_lyrics():
    print_lyrics()
    print('Na - na - na - na - na, na - na - na - na')
    print_lyrics()
repeat_lyrics()

def print_twice(whatever_name):
    print(whatever_name)
    print(whatever_name)

# print_twice = 'boo' (doesn't work since print_twice is only defined for "whatever_name")
her_name = 'geraldine'
print_twice(her_name)

def cat_twice(part1,part2):
    cat = part1 + part2
    print_twice(cat)

line1 = 'g s'
line2 = 's g'
cat_twice(line1, line2)

def give_me_a_break():
    str1 = 'break'
    return str1
print(give_me_a_break())



