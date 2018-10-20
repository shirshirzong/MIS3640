def get_price(item):
    price = 0
    for letter in item:
        if letter.isalpha():
            price += ord(letter) - 96
    return price

# print(get_price('bananas'))
# print(get_price('potato chips'))


def print_receipt(items):
    total_price = 0
    longest_word = max(items, key=len)
    width = len(longest_word)
    for item in items:
        price = get_price(item)
        print('{:<{number_length}}  ${:>6,.2f}'.format(
            item, price, number_length=width))
        total_price += price

    print('-' * (width + 9))
    print('{:<{number_length}}  ${:>6,.2f}'.format(
        'Total', total_price, number_length=width))


items = ['bananas', 'rice', 'paprika', 'potato chips']

print_receipt(items[:3])
