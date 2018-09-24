#Exercise 3
import math

def mysqrt(a):
    
    epsilon = 0.000000000000000001
    x = 1
    while True:
        y = (x + a / x) / 2
        if abs(y - x) < epsilon:
            break
        x = y
    return x


def test_square_root(n):

    print('{:3} {:14} {:14} {:14}'.format(
        'a', 'mysqrt(a)', 'math.sqrt(a)', 'diff'))
    print('{:3} {:14} {:14} {:14}'.format(
        '-', '---------', '------------', '----'))
    for a in range(1, n):
        print('{:3.1f} {:<14.12g} {:<14.12g} {:<14.12g}'.format(a, mysqrt(a),
                                                                math.sqrt(a), abs(mysqrt(a) - math.sqrt(a))))


test_square_root(10)

