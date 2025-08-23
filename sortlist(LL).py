class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

def sortlist(head):
    arr=[]
    temp=head
    while(temp):
        arr.append(temp.val)
        temp=temp.next
    arr.sort
    ind=0
    temp=head
    while(temp):
        temp.val=arr[ind]
        ind+=1
        temp=temp.next
    return head
head=[4,2,1,3,5]
print(sortlist(head))
