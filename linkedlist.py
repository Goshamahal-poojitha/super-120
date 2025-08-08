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
    printLinkedList(head)
def printLinkedList(head):
    temp = head
    while temp:
        print(temp.val, end="")
        if temp.next:
            print(" -> ", end="")
        temp = temp.next
    print()  
arr=list(map(int,input().split())) #1 2 3 4 5
createlinkedlist(arr)
