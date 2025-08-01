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
    print(firstnode(head))
def firstnode(head):
    slow=head
    fast=head
    while(fast and fast.next):
        slow=slow.next
        fast=fast.next.next
        if(slow==fast):
            fast=head
            while(True):
                if(slow==fast):
                    return slow
                slow=slow.next
                fast=fast.next
    return None 
arr=list(map(int,input().split()))
createlinkedlist(arr)