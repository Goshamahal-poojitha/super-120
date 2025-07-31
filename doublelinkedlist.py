class Node:
    def __init__(self,data):
        self.val=data
        self.next=None
        self.prev=None
def createDoublelinkedlist(arr):
    head=None
    for data in arr:
        if(head==None):
            head=Node(data)
            temp=head
        else:
            newnode = Node(data)
            temp.next=newnode
            newnode.prev=temp
            temp=temp.next
    printdoublell(head)
def printdoublell(head):
    temp=head
    while(temp):
        print(temp.val,end=" ")
        if temp.next:
            print(" <-> ", end="")
        temp=temp.next
    print()
        
arr=list(map(int,input().split())) #1 2 3 5 6
createDoublelinkedlist(arr)


