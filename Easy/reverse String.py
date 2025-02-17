Write a function that reverses a string. The input string is given as an array of characters s.

You must do this by modifying the input array in-place with O(1) extra memory.

Example 1:

Input: s = ["h","e","l","l","o"]
Output: ["o","l","l","e","h"]
Example 2:

Input: s = ["H","a","n","n","a","h"]
Output: ["h","a","n","n","a","H"]
 

Constraints:

1 <= s.length <= 105
s[i] is a printable ascii character.

Solution: Using in-place algorithm

Explanation: An in-place algorithm is one that solves a problem by modifying the input data directly, using only a small, 
constant amount of extra memory (usually O(1) space). 
It avoids creating copies of the input or using large additional data structures, making it memory-efficient. 
Examples include reversing an array or swapping elements in place.


class Solution:
    def reverseString(self, s: List[str]) -> None:
        """
        Do not return anything, modify s in-place instead.
        """
        l = len(s)
        for i in range(l // 2):
            s[i], s[l - 1 - i] = s[l - 1 - i], s[i]
        

