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


def squares(n):
    dictionary = {}
    for element in range(1, n+1):
        dictionary[element] = element ** 2
    return dictionary


print(squares(5))


def max_value(dict):
    list = []
    for element in dict:
        list.append(element)
    return max(list)


dict = {
    'a': 5, 'b': 4, 'c': 2, 'd': 10, 'e': 4
}
print(max_value(dict))
