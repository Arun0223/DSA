class Node:
    def __init__(self , value):
        self.value = value
        self.next = None

class Linked_list:
    def __init__(self,value):
        new_node=Node(value)
        self.head=new_node
        self.tail=new_node
        self.length=1
    def print_list(self):
        temp=self.head
        while temp is not None:
            print(temp.value)
            temp=temp.next
    def apend(self,value):
        new_node=Node(value)
        self.tail.next=new_node
        self.tail=new_node
        self.length+=1


ll=Linked_list(9)
ll.apend(10)
ll.apend(11)
ll.apend(12)


print(ll.head.value)
print(ll.tail.value)
if ll.head.next is None:
    print("ll.head.next:",None)
else:
    print(ll.head.next)
ll.print_list()
print(ll.length)
,


