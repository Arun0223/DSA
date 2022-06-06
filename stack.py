class Node:
    def __init__(self,value):
        self.value = value
        self.next=None
class Stack:
    def __init__(self,value):
        new_node=Node(value)
        self.top=new_node
        self.bottom=new_node
        self.length=1
    def print_stack(self):
        if self.length==0:
            return None
        else:
            temp=self.top
            while temp:
                print(temp.value)
                temp=temp.next
    def push(self,value):
        new_node=Node(value)
        if self.length==0:
            self.top=new_node
            self.bottom=new_node
            self.length=1
        else:
            new_node.next=self.top
            self.top=new_node
            self.length+=1

    def pop(self):
        if self.length==0:
            return None
        else:
            temp=self.top
            self.top=temp.next
            temp.next=None
            self.length-=1






