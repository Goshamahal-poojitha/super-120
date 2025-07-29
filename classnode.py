class Node:
    def __init__(self,data):
        self.val=data
        self.next=None
def createlinkedlist(arr):
    head=None
    for data in arr:
        if(head==None):
            head=Node(data)
            temp=head
        else:
            temp.next=Node(data)
            temp=temp.next
        print(countNodesinloop(head))
def countNodesinloop(head):
    slow=head
    fast=head
    while(fast and fast.next):
        slow=slow.next
        fast=fast.next.next
        if(slow==fast):
            fast=head
            c=1
            while(True):
                if(slow==fast):
                    while(True):
                        fast=fast.next
                        if(slow==fast):
                            return c
                        c+=1
                slow=slow.next
                fast=fast.next
    return 0
arr=list(map(int,input().split()))
createlinkedlist(arr)