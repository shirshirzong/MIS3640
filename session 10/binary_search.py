def binary_search(my_list, x):
    '''
    this function adopts bisection/binary search to find the index of a given
    number in an ordered list
    my_list: an ordered list of numbers from smallest to largest
    x: a number
    returns the index of x if x is in my_list, None if not.
    '''

    mid = len(my_list)//2
    #// is floor division that rounds down to the smaller integer of the result
    try:
        if my_list.index(x) > mid:
            place = binary_search(my_list[mid:],x)
            if place:
                return place+mid
        elif my_list.index(x) < mid:
            return binary_search(my_list[:mid],x)
        return mid        
    except ValueError:
        return None



test_list = [1, 3, 5, 235425423, 23, 6, 0, -23, 6434]
test_list.sort()
# print(test_list)
# print(test_list[3:].index(6)) -- from index 3, it starts to count index 3 as 0

print(binary_search(test_list, -23))
print(binary_search(test_list, 0))
print(binary_search(test_list, 235425423))
print(binary_search(test_list, 30))

# expected output
# 0
# 1
# 8
# None