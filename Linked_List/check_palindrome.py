from total_functionality import LL,Node
def check_palin(head):
    lst=[]
    temp=head
    while(temp):
        lst.append(temp.data)
        temp=temp.next
    for i in range(0,int(lst.__len__()/2)):
        x=lst.pop()
        if x==head.data:
            print("crct")
        else:
            return False
        head=head.next
    return True
if __name__ == '__main__':
    ll1=LL()
    ll1.push(5)
    ll1.push(15)
    ll1.push(25)
    ll1.push(25)
    ll1.push(75)
    ll1.push(5)
    a=check_palin(ll1.head)
    if a:
        print("yes")
    else:
        print("no")