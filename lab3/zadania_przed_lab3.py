# zad1

for number in range(101):
    if (number % 3 == 0 and number % 5 == 0):
        print("fizzbuzz")
    elif (number % 3 == 0 and number % 5 != 0):
        print("fizz")
    elif (number % 3 != 0 and number % 5 == 0):
        print("buzz")
    else:
        print(number)


# zad2

def part_list(list):
    i = (len(list)) - 2
    part = []
    while i >= 0:
        part.append(list[i])
        i = i - 3
    return part


list = [1, 2, 3, 4, 5, 6, 7, 8, 9]

print(part_list(list))

# i = (len(list)) - 1
# print(i)


def fibbonacci(number):
    if number <= 2:
        return 1
    else:
        return fibbonacci(number-2)+fibbonacci(number-1)


print(fibbonacci(5))


def word_counter(list):
    new_list = []
    for element in list:
        if len(element) > len(list[-1]):
            new_list.append(element)
    return len(new_list)


list = ['book', 'brush', 'wardrobe', 'handkerchief', 'orange']
print(word_counter(list))
