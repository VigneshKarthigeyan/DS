#Have data and two pointers in Node
#object 1.next 2.arbitary for sorting
class LL:
    def __init__(self):
        self.head=None
    def push(self,val):
        n1=Node(val)
        n1.next=self.head
        self.head=n1
    def middle(self,head):
        ones=head
        twos=head
        while twos.next1 and twos.next1.next1:
            ones=ones.next1
            twos=twos.next1.next1
        return ones

    def copyll(self,head):
        temp = head
        while temp:
            temp.next1 = temp.next
            temp = temp.next
        return self.merge_sort(head)
    def merge_sort(self,head):
        if head==None or head.next1==None:
            return head
        mid=self.middle(head)
        nextmid=mid.next1
        mid.next1=None
        left=self.merge_sort(head)
        right=self.merge_sort(nextmid)
        newll_head=self.merge(left,right)
        return newll_head
    def merge(self,left,right):
        if left==None:
            return right
        if right==None:
            return left
        if left.data<=right.data:
            newll_head=left
            newll_head.next1=self.merge(left.next1,right)
        else:
            newll_head=right
            newll_head.next1=self.merge(left,right.next1)
        return newll_head
    def printll(self,head):
        temp=head
        while temp:
            print(temp.data,end=" ")
            temp=temp.next
        print()
    def printllnext1(self,head):
        temp=head
        while temp:
            print(temp.data,end=" ")
            temp=temp.next1
        print()
class Node:
    def __init__(self,val):
        self.data=val
        self.next=None
        self.next1=None
if __name__=="__main__":
    ll1=LL()
    ll1.head=Node(10)
    ll1.push(50)
    ll1.push(30)
    ll1.push(40)
    ll1.push(20)
    ll1.push(60)
    ll1.printll(ll1.head)
    ll1.printllnext1(n1)

