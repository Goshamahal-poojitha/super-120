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
   # printLinkedList(head)
    print(getMiddle(head))
def getMiddle(head):
    slow=head
    fast=head
    while(fast and fast.next):
        slow=slow.next
        fast=fast.next.next
    return slow.val
def printLinkedList(head):
    temp=head
    while(temp):
        print(temp.val,end=" ")
        temp=temp.next
    
        print('->',end=" ")
arr=list(map(int,input().split()))
createlinkedlist(arr)
                                               