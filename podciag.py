# zad 1
def max_progression(length, progression):
    subsequence = []
    progression.sort(reverse=True)
    try:
        for item in range(length):
            subsequence.append(progression[item])
        return subsequence
    except IndexError:
        if progression == []:
            return ('the list is empty')
        if length > len(progression):
            return ('the list is too short')


progression = [3, 6, 4, 1, 9, 6]
length = 2
print(max_progression(length, progression))
