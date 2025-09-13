Given head, the head of a linked list, determine if the linked list has a cycle in it.

There is a cycle in a linked list if there is some node in the list that can be reached again by continuously following the next pointer. Internally, pos is used to denote the index of the node that tail's next pointer is connected to. Note that pos is not passed as a parameter.

Return true if there is a cycle in the linked list. Otherwise, return false.

Example 1:

Input: head = [3,2,0,-4], pos = 1
Output: true
Explanation: There is a cycle in the linked list, where the tail connects to the 1st node (0-indexed).
Example 2:

Input: head = [1,2], pos = 0
Output: true
Explanation: There is a cycle in the linked list, where the tail connects to the 0th node.
Example 3:


Input: head = [1], pos = -1
Output: false
Explanation: There is no cycle in the linked list.

Solution: Using hashset

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        curr_node = head
        visited_node = set()
        
        while curr_node is not None:
            if curr_node in visited_node:
                return True
            visited_node.add(curr_node)
            curr_node = curr_node.next
        return False


Solution 2: Using Floyd's cycle detection

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        slow_pointer, fast_pointer = head, head
        while fast_pointer and fast_pointer.next:
            slow_pointer = slow_pointer.next
            fast_pointer = fast_pointer.next.next
            if slow_pointer == fast_pointer:
                return True
        return False
        

        

        
