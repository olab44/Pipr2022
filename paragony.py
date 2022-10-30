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

receipt= [
    ('apples', 233), ('bananas', 499), ('oranges', 802), ('milk', 312)
]
# receipt.append(get_product())
# receipt.append(get_product())
# receipt.append(get_product())

# for element in receipt:
#     print_description(element[0], element[1])

def get_total_price():
    total_price = 0
    for element in receipt:
        total_price=total_price+element[1]
    return f'total price is {total_price//100} zł {total_price%100} gr'
        

print(get_total_price())