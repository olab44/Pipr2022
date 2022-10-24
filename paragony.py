def get_description (name,price):
    price_zl=price//100
    price_gr=price%100
    return f' price of {name} is {price_zl}.{price_gr:02}'
def print_description (name,price): 
    description=get_description (name,price)
    print(description)
    
print_description('Oranges', 901)

