class Node:
    def __init__(self,v1,v2):
        self.x=v1
        self.y=v2
        self.next=None
class LL:
    def __init__(self):
        self.head=None
    def push(self,v1,v2):
        n_node=Node(v1,v2)
        n_node.next=self.head
        self.head=n_node
    def middle(self):
        if self.head==None or self.head.next==None or self.head.next.next==None:
            return self.head
        pre = self.head
        cur = pre.next
        suf = cur.next
        if pre.x == cur.x:
            print("x equals")
            print(suf.x)
            while suf and cur.x == suf.x:
                print(cur.x,suf.x)
                pre.next = suf
                cur = suf
                suf = suf.next
                print(cur.x,suf.x)
                self.printll()
        elif pre.y == cur.y:
            print("y equals")
            while suf and cur.y == suf.y:
                print(cur.y,suf.y)
                pre.next = suf
                cur = suf
                suf = suf.next
                self.printll()
        else:
            print("The given segments are not valid")
            return
        temp=self.head
        self.head=self.head.next
        print("dg")
        self.middle()
        self.head=temp
        return self.head
    def printll(self):
        temp = self.head
        while temp:
            print("(%d,%d)" % (temp.x, temp.y), end=" ")
            temp = temp.next
        print()
if __name__ == '__main__':
    ll1 = LL()
    ll1.head = Node(40, 5)
    ll1.push(20, 5)
    ll1.push(10,5)
    ll1.push(10,8)
    ll1.push(10, 10)
    ll1.push(3, 10)
    ll1.push(1, 10)
    ll1.push(0,10)
    ll1.printll()
    ll1.middle()
    ll1.printll()
