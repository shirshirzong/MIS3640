def quad():
    from math import sqrt
    print('Let me solve your quadratic equation')
    a = int(input('please input the first coefficient:'))
    b = int(input('please input the second coefficient:'))
    c = int(input('please input the second coefficient:'))
    print()
    disc = b ** 2 - 4 * a * c #b^2 - 4ac
    disc1 = sqrt(disc)
    positive = (-b + disc1) / (2*a)
    negative = (-b - disc1) / (2*a)

    print('the positive value of the quadratic equation is {0}, and then negative value is {1}'.format(positive,negative))

quad()