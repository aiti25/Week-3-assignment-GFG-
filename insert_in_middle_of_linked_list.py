'''
    Your task is to insert a new node in 
	the middle of the linked list with
	the given value.
	
	{
		# Node Class
		class Node:
		    def __init__(self, data):   # data -> value stored in node
		        self.data = data
		        self.next = None
	}
	
	Function Arguments: head (head of linked list), node 
	(node to be inserted in middle)
	Return Type: None, just insert the new node at mid.
'''
#Function to insert a node in the middle of the linked list.

class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


class Solution:
    def insertInMiddle(self, head, x):
        new_node = Node(x)

       
        if head is None:
            head = new_node
            return head

    
        slow = head
        fast = head

        while fast.next and fast.next.next:
            slow = slow.next
            fast = fast.next.next

     
        new_node.next = slow.next
        slow.next = new_node

        return head