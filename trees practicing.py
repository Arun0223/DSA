class Node:
    def __init__(self,value):
        self.value=value
        self.left=None
        self.right=None
class BSTT:
    def __init__(self):
        self.root=None
    def insert(self,value):
        new_node=Node(value)
        if self.root==None:
            self.root=new_node
            return True
        temp=self.root
        while True:
            if new_node.value==temp.value:
                return False
            elif new_node.value < temp.value:
                if temp.left is None:
                    temp.left=new_node
                    return True
                temp=temp.left
            else:
                if temp.right is None:
                    temp.right=new_node
                    return True
                temp=temp.right
    def contains(self,value):
        temp=self.root
        while temp is not None:
            if value<temp.value:
                temp=temp.left
            elif value>temp.value:
                temp=temp.right
            else:
                return True
        return False
    def minimum(self,current_node):
        temp=current_node
        while temp.left is not None:
            temp=temp.left
        return temp.value
        else:
            temp = self.root
            while True:
                if new_node.value < temp.value:
                    if temp.left is None:
                        temp.left=new_node
                        return True
                    temp=temp.left
                elif new_node>temp.value:
                    if temp.right is None:
                        temp.right = new_node
                        return True
                    temp=temp.right
                else:
                    return False


b=BST()
b.insert(100)


