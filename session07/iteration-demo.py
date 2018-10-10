# result = 0

# for i in range(10):
#     print('current number to be added"',i+1)
#     result = result + i + 1
#     print('new result after this iteration:',result)

# print('The final result:', result)

# result = 0

# for i in range(1,1001):
#     if i % 2 == 1:
#         result = result + i
# print('The sum of odd number is', result)

import time

def countdown(n):
    while n>0:
        print(n)
        time.sleep(1)
        n = n - 1
    print('Blastoff!')

countdown(10)