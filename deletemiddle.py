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

    deleteMiddle(head)
    printLinkedList(head)
def deleteMiddle(head):
    if(head.next==Node):
        return None
    slow=head
    fast=head
    while(fast and fast.next):
        prev=slow
        slow=slow.next
        fast=fast.next.next
    prev.next=slow.next
    slow.next=None
    return head 
def printLinkedList(head):
    temp=head
    while(temp):
        print(temp.val,end=" ")
        if temp.next:
            print(" -> ", end="")
        temp=temp.next
    
    print()
arr=list(map(int,input().split())) #1 2 3 4 5
createlinkedlist(arr)
                                               