class Node:
    def __init__(self, value):
        self.value = value
        self.next = None
        self.prev = None


class DoublyLinkedList:
    def __init__(self, value):
        new_node = Node(value)
        self.head = new_node
        self.tail = new_node
        self.length = 1

    def printList(self):
        if self.length == 0:
            return None
        else:
            temp = self.head
            while temp:
                print(temp.value)
                temp = temp.next

    def apend(self, value):
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
            self.length -= 1
        else:
            temp = self.tail.prev
            self.tail.prev = None
            temp.next = None
            self.tail = temp
            self.length -= 1

    def popfirst(self):
        if self.length == 0:
            return None
        elif self.length == 1:
            self.head = None
            self.tail = None
            self.length -= 1
        else:
            temp = self.head
            self.head = self.head.next
            self.head.prev = None
            temp.next = None
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

    def get(self, index):
        if index < 0 or index >= self.length:
            return None
        else:
            temp = self.head
            for i in range(index):
                temp = temp.next
            return temp

    def set_value(self, index, value):
        temp = self.get(index)
        temp.value = value

    def insert(self, index, value):
        if index < 0 or index > self.length:
            return None
        elif index == 0:
            return self.prepend(value)
        elif index == self.length:
            return self.apend(value)
        else:
            new_node = Node(value)
            prev = self.get(index - 1)
            after = self.get(index)
            prev.next = new_node
            new_node.prev = prev
            after.prev = new_node
            new_node.next = after
            self.length += 1

    def remove(self, index):
        if index < 0 or index >= self.length:
            return None
        elif index == 0:
            return self.popfirst()
        elif index == self.length - 1:
            return self.pop()
        else:
            temp = self.get(index - 1)
            next1 = self.get(index + 1)
            temp.next = next1
            next1.prev = temp
            self.length -= 1

## ******************************************************************************** ##

class Node:
    def __init__(self, value):
        self.value = value
        self.next = None
        self.prev = None


class DLL:
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
            new_node.prev = self.tail
            self.tail = new_node
        self.length += 1

    def pre_pend(self, value):
        new_node = Node(value)
        if self.length == 0:
            self.head = new_node
            self.tail = new_node
        else:
            new_node.next = self.head
            self.head.prev = new_node
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
            self.tail.prev = None
            self.tail = prev
            self.tail.next = None
            self.length -= 1

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
            return False
        temp = self.head
        for i in range(index):
            temp = temp.next
        return temp

    def set_item(self, index, value):
        if index < 0 or index >= self.length:
            return False
        temp = self.get_item(index)
        temp.value = value

    def insert(self, index, value):
        if index < 0 or index > self.length:
            return False
        elif index == 0:
            return self.pre_pend(value)
        elif index == self.length - 1:
            return self.append(value)
        else:
            new_node = Node(value)
            temp = self.get_item(index - 1)
            after = self.get_item(index)
            temp.next = new_node
            new_node.next = after
            after.prev = new_node
            new_node.prev = temp
            self.length += 1

    def remove(self, index):
        if index < 0 or index >= self.length:
            return False
        elif index == 0:
            return self.pop_first()
        elif index == self.length - 1:
            return self.pop()
        else:
            temp = self.get_item(index - 1)
            after = self.get_item(index + 1)
            temp.next = after
            after.prev = temp
            self.length -= 1












