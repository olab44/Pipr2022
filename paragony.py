def split_price(price):
    price_zl = price // 100
    price_gr = price % 100
    return (price_zl, price_gr)


def get_description(name, price):
    price_parts = split_price(price)
    return f' price of {name} is {price_parts[0]}.{price_parts[1]:02}'


def print_description(name, price):
    description = get_description(name, price)
    print(description)


# print_description('apples', 203)


def get_product():
    name = input("enter product name: ")
    price = input("how many?: ")

    return name, price


product = get_product()
# print_description(product[0], product[1])

# for element in receipt:
#     print_description(element[0], element[1])


def get_total_price(receipt):
    total_price = 0
    for name, price in receipt:
        total_price += price
    return total_price


def format_price(price):
    zl, gr = split_price(price)
    return f'{zl}.{gr}'


def print_receipt(date, receipt):

    if not receipt:
        print("Paragon jest pusty")
        return
    else:
        position = 1
        print(date)
        for name, price in receipt:
            price = format_price(price)
            tax_group = get_tax_group(name)
            print(f'{position:2}. {name:19} {price:>6} {tax_group}')
            position += 1
        print('-'*30)
        count_tax(name)
        total_value = get_total_price(receipt)
        formated_value = format_price(total_value)
        print(f'total {formated_value:>25}')


def count_tax(name):
    price = format_price(price)
    if get_tax_group(name) == 'A':
        return price * tax_prices[0]
    elif get_tax_group(name) == 'B':
        return price * tax_prices[1]
    else:
        return (price * tax_prices[2])


print(count_tax('bananas'))


def get_tax_group(name):
    if name in tax_groupA:
        return 'A'
    elif name in tax_groupB:
        return 'B'
    elif name in tax_groupC:
        return 'C'
    elif name in tax_groupD:
        return 'D'
    else:
        return 'E'


product_prices = {
    'bananas': 499,
    'oranges': 532,
    'milk': 233
    }

my_receipt = [
    ('apples', 233),
    ('bananas', 499),
    ('oranges', 3842),
    ('milk', 312)
]


tax_groupA = {'milk', 'bread'}
tax_groupB = {'apples', 'bananas', 'oranges'}
tax_groupC = {'water', 'juice'}
tax_groupD = {'phone', 'headphones'}

# print(get_tax_group('beer'))

# if not my_receipt:
#     print("receipt is empty")
# else:
#     print_receipt('2022-10-30', my_receipt)


print_receipt('2022-10-30', my_receipt)
my_total_value = get_total_price(my_receipt)

tax_prices = {'A': 0.12, 'B': 0.8, 'E': 0.22}
