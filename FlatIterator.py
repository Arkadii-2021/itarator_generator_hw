nested_list = [
    ['a', 'b', 'c'],
    ['d', 'e', 'f'],
    [1, 2, None]
]


class FlatIterator:
    def __init__(self, n_list):
        self.n_list = n_list
        self.index_1 = 0
        self.index_2 = -1

    def __iter__(self):
        return self

    def __next__(self):
        self.index_2 += 1
        if self.index_2 == len(nested_list[self.index_1]):
            self.index_2 = 0
            self.index_1 += 1
            if self.index_1 == len(nested_list):
                raise StopIteration
        return self.n_list[self.index_1][self.index_2]


if __name__ == '__main__':
    for item in FlatIterator(nested_list):
        print(item)
