def split_price(price):
    price_zl=price//100
    price_gr=price%100
    return(price_zl, price_gr)

def get_description (name,price):
    price_parts= split_price(price)
    return f' price of {name} is {price_parts[0]}.{price_parts[1]:02}'

def print_description (name,price): 
    description=get_description (name,price)
    print(description)

# print_description('apples', 203)

def get_product():
    name = input("enter product name: ")
    price =input("enter product price: ")
    return name, int(price)

product = get_product()
# print_description(product[0], product[1])

# for element in receipt:
#     print_description(element[0], element[1])

def get_total_price(receipt):
    total_price = 0
    for name,price in receipt:
        total_price+=price
    return total_price

def format_price(price):
    zl, gr =split_price(price)
    return f'{zl}.{gr}'
        
my_receipt= [
    ('apples', 233), 
    ('bananas', 499), 
    ('oranges', 802), 
    ('milk', 312)
]
my_total_value = get_total_price(my_receipt)
print(format_price(my_total_value))