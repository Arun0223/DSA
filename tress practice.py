class Node:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None


class Bsy1:
    def __init__(self):
        self.root = None

    def insert(self, value):
        new_node = Node(value)
        if self.root == None:
            self.root = new_node
            return True
        temp = self.root
        while True:
            if new_node.value < temp.value:
                if temp.left is None:
                    temp.left = new_node
                    return True
                temp = temp.left
            elif new_node.value > temp.value:
                if temp.right is None:
                    temp.right = new_node
                    return True
                temp = temp.right
            else:
                return False

    def contains(self, value):
        if self.root == None:
            return False
        temp = self.root
        while True:
            if value < temp.value:
                temp = temp.left
            elif value > temp.value:
                temp = temp.right
            else:
                return True

    def minimum(self, current_node):
        temp = current_node
        while temp.left is not None:
            temp = temp.left
        return temp.value
