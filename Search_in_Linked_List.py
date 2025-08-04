#User function Template for python3


''' Node of a linked list 
class Node:
    def __init__(self, data):
        self.data = data
        self.next = None
'''
class Solution:

    def searchKey(self, n, head, key):
        current = head
        
        # Traverse the linked list
        while current:
            if current.data == key:
                return True
            current = current.next
        
        return False
