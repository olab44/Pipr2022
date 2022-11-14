if __name__ == '__main__':
    n = int(input())
    integer_list = map(int, input().split())
    

def tuples_hash(n, integer_list):
    new_list = []
    for element in integer_list:
        value = hash(element)
        new_list.append(value)
    return (new_list)


print(tuples_hash(n, integer_list))