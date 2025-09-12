Given the head of a singly linked list, reverse the list, and return the reversed list.
Example 1:


Input 1: head = [1,2,3,4,5]
Output: [5,4,3,2,1]
Example 2:

Input 2: head = [1,2]
Output: [2,1]
Example 3:

Input 3: head = []
Output: []

Solution: Using two pointer approach

class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        prev, curr = None, head
        while curr:
            nxt = curr.next
            curr.next = prev
            prev = curr
            curr = nxt
        return prev

Explanation: 

prev: The node that comes before the current node in the reversed list.
curr: The node we are currently processing.
nxt: Temporarily stores curr.next so we don't lose the rest of the original list.
