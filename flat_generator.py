nested_list = [
    ['a', 'b', 'c'],
    ['d', 'e', 'f'],
    [1, 2, None]

]


def my_range(start, end):
    while start <= end:
        yield start
        start += 1


def flat_generator():
    index_1 = 0
    index_2 = 0
    index_3 = len(nested_list)
    while index_1 < index_3:
        yield nested_list[index_1][index_2]
        index_2 += 1
        if index_2 >= len(nested_list[index_1]):
            index_2 = 0
            index_1 += 1
            if index_1 > index_3:
                break


if __name__ == '__main__':
    for item in flat_generator():
        print(item)
