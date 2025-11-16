
from typing import Optional

# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def isPalindrome(self, head: Optional[ListNode]) -> bool:
        # Initialize a stack to store the first half of the list
        stack = []
        slow = fast = head

        # Traverse the list to find the midpoint
        while fast and fast.next:
            stack.append(slow.val)
            slow = slow.next
            fast = fast.next.next

        # If the list has an odd number of elements, skip the middle element
        if fast:
            slow = slow.next

        # Compare the second half of the list with the values in the stack
        while slow:
            if stack.pop() != slow.val:
                return False
            slow = slow.next

        return True
