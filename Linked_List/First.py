#Creating class for Linked list
#Print function
class Linked_List:
    def __init__(self):
        self.head=None
    def Printll(self):
        temp=self.head
        while(temp!=None):
            print(temp.data)
            temp=temp.next

class Node:
    def __init__(self,data):
        self.data=data
        self.next=None

if __name__ == '__main__':
    obj=Node(5)
    obj2=Node(10)
    obj3 = Node(15)
    obj4 = Node(20)
    obj5 = Node(30)
    ll=Linked_List()
    ll.head=obj
    obj.next=obj2
    obj2.next = obj3
    obj3.next = obj4
    obj4.next = obj5
    ll.Printll()