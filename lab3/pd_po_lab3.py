# zad 1

def count_symbols(list):
    symbol_counter = {}
    pre_list = []
    for element in list:
        pre_list += element
    for letter in pre_list:
        if letter not in symbol_counter:
            symbol_counter[letter] = 0
        symbol_counter[letter] += 1
    return symbol_counter


list = [['a', 'c', 'o'], ['a', 'a', 'c'], ['d', 'o', 'O'], ['c', 'b', 'a']]
print(count_symbols(list))


# zad 2


def time_description(hour, minute):
    if minute == 0:
        return f'{}'




minutes_dic = {
    0: "o' clock",
    15: 'quater',
    30: 'past',
    1: 'one minute',
    

}

print(time_description(1,0))