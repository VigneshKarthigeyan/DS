from total_functionality import LL,Node
def find_loop(ll1):
    slow=ll1
    fast=ll1.next
    while(fast and fast.next):
        if slow==fast:
            print("loop exist at ",slow.data)
            break
        slow=slow.next
        fast=fast.next.next
    print(slow.data)
if __name__ == '__main__':
    ll1=LL()
    ll1.push(14)
    ll1.push(20)
    ll1.push(23)
    ll1.push(30)
    ll1.push(35)
    ll1.push(40)
    ll1.head.next.next.next=ll1.head.next
    find_loop(ll1.head)
    ll1.printll()