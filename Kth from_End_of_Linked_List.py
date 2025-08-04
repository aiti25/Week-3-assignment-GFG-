'''
	{
		# Node Class
		class Node:
		    def __init__(self, data):   # data -> value stored in node
		        self.data = data
		        self.next = None
	}
'''
class Solution:
    def getKthFromLast(self, head, k):
        #code here
        fast = head
        slow = head

        # Move fast pointer k steps ahead
        for _ in range(k):
            if not fast:
                return -1  # k is greater than the number of nodes
            fast = fast.next

        # Move both pointers until fast reaches the end
        while fast:
            slow = slow.next
            fast = fast.next

        return slow.data if slow else -1