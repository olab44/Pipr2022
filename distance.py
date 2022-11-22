
def distance(n, point_1, point_2):
    x_1, y_1 = point_1
    x_2, y_2 = point_2
    if point_1 == (n, y_1) and point_2 == (-n, y_2):
        return 0
    if point_1 == (x_1, n) and point_2 == (x_1, -n):
        return 0
    half = n / 2
    if x_1 > half:
        x_1 = - x_1
    if x_2 > half:
        x_2 = - x_2
    if y_1 > half:
        y_1 = - y_1
    if y_1 > half:
        y_2 = - y_2
    length_x = x_2 - x_1
    length_y = y_2 - y_1
    return abs(length_x) + abs(length_y)


point_1 = (3, 4)
point_2 = (1, 0)
print(distance(6, point_1, point_2))
