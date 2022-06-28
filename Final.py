class Node:
    def __init__(self, value):
        self.value = value
        self.next = None


class LLL:
    def __init__(self, value):
        new_node = Node(value)
        self.head = new_node
        self.tail = new_node
        self.length = 1

    def print_list(self):
        if self.length == 0:
            return None
        else:
            temp = self.head
            while temp is not None:
                print(temp.value)
                temp = temp.next

    def append(self, value):
        new_node = Node(value)
        if self.length == 0:
            self.head = new_node
            self.tail = new_node
        else:
            self.tail.next = new_node
            self.tail = new_node
        self.length += 1

    def pop(self):
        if self.length == 0:
            return None
        temp = self.head
        while temp.next is not None:
            prev = temp
            temp = temp.next
        self.tail = prev
        self.tail.next = None
        self.length -= 1

    def prepend(self, value):
        new_node = Node(value)
        if self.length == 0:
            self.head = new_node
            self.tail = new_node
        else:
            new_node.next = self.head
            self.head = new_node
        self.length += 1

    def pop_first(self):
        if self.length == 0:
            return None
        else:
            temp = self.head
            self.head = temp.next
            temp.next = None
            self.length -= 1

    def get_item(self, index):
        if index < 0 or index >= self.length:
            return False
        else:
            temp = self.head
            for _ in range(index):
                temp = temp.next
            return temp

    def set_item(self, index, value):
        if index < 0 or index >= self.length:
            return False
        else:
            temp = self.get_item(index)
            temp.value = value
            return True

    def insert(self, index, value):
        if index < 0 or index > self.length:
            return False
        elif index == 0:
            return self.prepend(value)
        elif index == self.length:
            return self.append(value)
        else:
            new_node = Node(value)
            temp = self.get_item(index - 1)
            new_node.next = temp.next
            temp.next = new_node
            self.length += 1

    def remove(self, index):
        if index < 0 or index >= self.length:
            return False
        elif index == 0:
            return self.pop_first(value)
        elif index == self.length - 1:
            return self.pop(value)
        else:
            before = self.get_item(index - 1)
            after = self.get_item(index + 1)
            temp = self.get_item(index)
            before.next = after
            temp.next = None
            self.length -= 1

    def reverse(self):
        if self.length == 0:
            return False
        else:
            temp = self.head
            self.head = self.tail
            self.tail = temp
            after = temp.next
            before = None
            for i in range(self.length):
                after = temp.next
                temp.next = before
                before = temp
                temp = after


class DNODE:
    def __init__(self, value):
        self.value = value
        self.next = None
        self.prev = None


class DL:
    def __init__(self, value):
        new_node = DNODE(value)
        self.head = new_node
        self.tail = new_node
        self.length = 1

    def print_list(self):
        if self.length == 0:
            return None
        else:
            temp = self.head
            while temp is not None:
                print(temp.value)
                temp = temp.next

    def append(self, value):
        new_node = Node(value)
        if self.length == 0:
            self.head = new_node
            self.tail = new_node
        else:
            self.tail.next = new_node
            new_node.prev = self.tail
            self.tail = new_node
            self.length += 1

    def pop(self):
        if self.length == 0:
            return None
        elif self.length == 1:
            self.head = None
            self.tail = None
            self.length = 0
        else:
            temp = self.head
            while temp.next is not None:
                prev = temp
                temp = temp.next
            self.tail.prev = None
            prev.next = None
            self.tail = prev
            self.length -= 1

    def prepend(self, value):
        new_node = Node(value)
        if self.length == 0:
            self.head = new_node
            self.tail = new_node
        else:
            new_node.next = self.head
            self.head.prev = new_node
            self.head = new_node
        self.length += 1

    def pop_first(self):
        if self.length == 0:
            return None
        else:
            temp = self.head
            self.head = temp.next
            self.head.prev = None
            temp.next = None
            self.length -= 1

    def get_item(self, index):
        if index < 0 or index >= self.length:
            return None
        temp = self.head
        for _ in range(index):
            temp = temp.next
        return temp

    def set_item(self, index, value):
        if index < 0 or index >= self.length:
            return None
        temp = self.get_item(index)
        temp.value = value

    def insert(self, index, value):
        if index < 0 or index > self.length:
            return None
        elif index == 0:
            return self.prepend(value)
        elif index == self.length:
            return self.append(value)
        new_node = Node(value)
        temp = self.get_item(index - 1)
        after = temp.next
        new_node.next = after
        after.prev = new_node
        new_node.prev = temp
        temp.next = new_node
        self.length += 1

    def remove(self, index):
        if index < 0 or index >= self.length:
            return None
        elif index == 0:
            return self.pop_first(value)
        elif index == self.length - 1:
            return self.pop(value)
        else:
            prev = self.get_item(index - 1)
            after = self.get_item(index + 1)
            prev.next = after
            after.prev = prev
            self.length -= 1


class SNODE:
    def __init__(self, value):
        self.value = value
        self.next = None


class Stack:
    def __init__(self, a):
        new_node = SNODE(a)
        self.top = new_node
        self.bottom = new_node
        self.length = 1

    def print_stack(self):
        if self.length == 0:
            return None
        else:
            temp = self.top
            while temp is not None:
                print(temp.value)
                temp = temp.next

    def push(self, value):
        new_node = Node(value)
        if self.length == 0:
            self.top = new_node
            self.bottom = new_node
        else:
            new_node.next = self.top
            self.top = new_node
        self.length += 1

    def pop(self):
        if self.length == 0:
            return None
        else:
            temp = self.top
            self.top = temp.next
            temp.next = None
            self.length -= 1


class Qnode:
    def __init__(self, value):
        self.value = value
        self.next = None


class Queue:
    def __init__(self, value):
        new_node = Qnode(value)
        self.first = new_node
        self.last = new_node
        self.length = 1

    def print_queue(self):
        temp = self.first
        while temp is not None:
            print(temp.value)
            temp = temp.next

    def enqueue(self, value):
        new_node = Node(value)
        if self.length == 0:
            self.first = new_node
            self.last = new_node
        else:
            self.last.next = new_node
            self.last = new_node
        self.length += 1

    def dequeue(self):
        if self.length == 0:
            return None
        else:
            temp = self.first
            self.first = temp.next
            temp.next = None
            self.length -= 1


class Tnode:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None


class Tree:
    def __init__(self):
        self.root = None

    def insert(self, value):
        new_node = Tnode(value)
        if self.root == None:
            self.root = new_node
            return True
        temp = self.root
        while True:

            if value == temp.value:
                return False
            elif value < temp.value:
                if temp.left is None:
                    temp.left = new_node
                    return True
                temp = temp.left
            else:
                if temp.right is None:
                    temp.right = new_node
                    return True
                temp = temp.right

    def contains(self, value):
        temp = self.root
        while True:
            if temp.value == value:
                return True
            elif value < temp.value:
                temp = temp.left
            elif value > temp.value:
                temp = temp.right
            else:
                return False

    def minimum(self, current_node):
        temp = current_node
        while temp.left is not None:
            temp = temp.left
        return temp.value


class Hash_Table:
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

    def insert(self, key, value):
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
        else:
            return False

    def get_keys(self):
        output = []
        for i in self.data_map:
            if i is not None:
                for j in i:
                    output.append(j[0])
        return output


class Graph:
    def __init__(self):
        self.adj_list = {}

    def print_graph(self):
        for i in self.adj_list:
            print(i, ":", self.adj_list[i])

    def add_vertex(self, vertex):
        if vertex in self.adj_list:
            return False
        else:
            self.adj_list[vertex] = []
            return True

    def add_edges(self, v1, v2):
        if v1 in self.adj_list and v2 in self.adj_list:
            self.adj_list[v1].append(v2)
            self.adj_list[v2].append(v1)

    def remove_edges(self, v1, v2):
        if v1 in self.adj_list and v2 in self.adj_list:
            if v1 in self.adj_list[v2] and v2 in self.adj_list[v1]:
                self.adj_list[v1].remove(v2)
                self.adj_list[v2].remove(v1)

    def remove_vertex(self, vertex):
        if vertex in self.adj_list:
            for i in self.adj_list[vertex]:
                self.adj_list[i].remove(vertex)
            del self.adj_list[vertex]
            return True
        return False

















