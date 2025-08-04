# your task is to complete this function
# function should return new head pointer

'''
class node:
    def __init__(self):
        self.data = None
        self.next = None
'''

def deleteNode(head, x):
   
    if x == 1:
        return head.next

   
    current = head
    for i in range(1, x - 1):
        if current is None or current.next is None:
            return head  
        current = current.next

    
    if current.next:
        current.next = current.next.next

    return head
