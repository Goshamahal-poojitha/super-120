class Node:
    def __init__(self,data):
        self.val=data
        self.next=None
def createll(arr):
    head=None
    for data in arr:
        if(head==None):
            head=Node(data)
            temp=head
        else:
            newnode = Node(data)
            temp.next=newnode
    deleteHead(head) 
    printdeletell(head)  
def deleteHead(head):
    temp=head.next
    head.next=None
    return temp
   
def printdeletell(head):
    temp=head
    while(temp):
        print(temp.val,end=" ")
        if temp.next:
            print(" -> ", end="")
        temp=temp.next
    
    print()
arr=list(map(int,input().split())) #1 2 3 4 5
createll(arr)
