# zad 1
def max_progression(length, progression):
    subsequence = []
    progression.sort(reverse=True)
    for item in range(length):
        subsequence.append(progression[item])
    return subsequence


progression = [3, 6, 4, 1, 9, 6]
length = 2
print(max_progression(length, progression))


# zad 2
def distance(point_1, point_2):
    x_1, y_1 = point_1
    x_2, y_2 = point_2
    if y_1 == y_2:
        return 0
    length_x = x_2 - x_1
    length_y = y_2 - y_1
    return abs(length_x) + abs(length_y)


point_1 = (3, 4)
point_2 = (1, 0)
print(distance(point_1, point_2))
