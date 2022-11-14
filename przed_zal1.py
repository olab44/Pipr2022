dic = {}
dic['pl'] = 8
print(dic)

dic_1 = {
    'oranges': 60, 'apples': 40, 'strawberries': 64
}

dic_2 = {
    'pl': 'Poland', 'it': 'Italy'
}

dic_3 = {
    'bl': 'black', 'rd': 'red'
}
if 'oranges' in dic_1:
    print(True)


# słownik kwadratów liczb
def squares(n):
    dictionary = {}
    for element in range(1, n+1):
        dictionary[element] = element ** 2
    return dictionary


print(squares(5))


# znajdowanie największej wartości w słowniku
def max_value(dict):
    list = []
    for element in dict:
        list.append(dict[element])
    return max(list)


dict = {
    'a': 5, 'b': 4, 'c': 2, 'd': 10, 'e': 4
}
print(max_value(dict))


# sumowanie wartości w słowniku


def sum_value(dict):
    list = []
    for element in dict:
        list.append(dict[element])
    return sum(list)


print(sum_value(dict))


# sprawdzanie czy istnieje klucz w słowniku
def checking(key):
    if key in dict:
        return dict[key]
    else:
        return ("There is not such key in this dictionary")


print(checking('5'))
