class Node:
    def __init__(self, value):
        self.value = value
        self.next = None


class LL:
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

    def prepend(self, value):
        new_node = Node(value)
        if self.length == 0:
            self.head = new_node
            self.tail = new_node
        else:
            new_node.next = self.head
            self.head = new_node
        self.length += 1

    def pop(self):
        if self.length == 0:
            return None
        else:
            temp = self.head
            while temp.next is not None:
                prev = temp
                temp = temp.next
            self.tail = prev
            self.tail.next = None
            self.length -= 1

    def pre_pop(self):
        if self.length == 0:
            return None
        else:
            temp = self.head
            self.head = temp.next
            temp.next = None
            self.length -= 1

    def get(self, index):
        if index < 0 or index >= self.length:
            return 'Index out of range'
        else:
            temp = self.head
            for i in range(index):
                temp = temp.next
            return temp

    def set_item(self, index, value):
        if index < 0 or index >= self.length:
            return 'Index out of range'
        else:
            temp = self.get(index)
            temp.value = value

    def insert(self, index, value):
        if index < 0 or index > self.length:
            return False
        elif index == 0:
            return self.prepend(value)
        elif index == self.length:
            return self.append(value)
        else:
            new_node = Node(value)
            prev = self.get(index - 1)
            new_node.next = prev.next
            prev.next = new_node
            self.length += 1

    def remove(self, index):
        if self.length == 0:
            return None
        else:
            if index < 0 and index >= self.length:
                return False
            elif index == 0:
                return self.pre_pop()
            elif index == self.length - 1:
                return self.pop()
            else:
                temp = self.get(index)
                before = self.get(index - 1)
                after = self.get(index + 1)
                before.next = after
                temp.next = None
                self.length -= 1

    def reverse(self):
        temp = self.head
        self.head = self.tail
        self.tail = temp
        after = temp.next
        before = None
        for _ in range(self.length):
            after = temp.next
            temp.next = before
            before = temp
            temp = after

