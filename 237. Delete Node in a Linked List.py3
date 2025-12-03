



# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def deleteNode(self, node):
        """
        Deletes the given node (except the tail) from the singly linked list.
        :type node: ListNode
        :rtype: void
        """
        if node is None or node.next is None:
            raise Exception("Cannot delete the last node or a null node with this method.")
        
        # Copy the value from the next node to the current node
        node.val = node.next.val
        # Bypass the next node
        node.next = node.next.next
