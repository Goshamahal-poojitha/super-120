def ispalindrome(head):
    arr=[]
    temp=head
    while(temp):
        arr.append(temp.val)
        temp=temp.next
    return arr==arr[::-1]
head=153
print(ispalindrome(head))
