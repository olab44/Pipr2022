def split_price(price):
    price_zl=price//100
    price_gr=price%100
    return(price_zl, price_gr)


def get_description (name,price):
    price_parts=(split_price(price))
    return f' price of {name} is {price_parts[0]}.{price_parts[1]:02}'

def get_product():
    name = input("enter product name: ")
    price =input("enter product price: ") 
    return name, int(price)

product = get_product()

def print_description (name,price): 
    description=get_product (name,price)
    print(description)

print_description(product[0], product[1])

