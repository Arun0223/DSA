class Hash:
    def __init__(self, size=7):
        self.data_map = [None] * size

    def print_table(self):
        for i, val in enumerate(self.data_map):
            print(i, ":", val)

    def __hash(self, key):
        my_hash = 0
        for i in key:
            my_hash = (my_hash + ord(i) * 23) % len(self.data_map)
        return my_hash

    def set_item(self, key, value):
        index = self.__hash(key)
        if self.data_map[index] is None:
            self.data_map[index] = []
        self.data_map[index].append([key, value])

    def get_item(self, key):
        index = self.__hash(key)
        if self.data_map[index] is not None:
            for i in self.data_map[index]:
                if i[0] == key:
                    return i[1]

    def keys(self):
        output = []
        for i in self.data_map:
            if i is not None:
                for j in i:
                    output.append(j[0])
        return output

