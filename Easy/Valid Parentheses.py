Given a string s containing just the characters '(', ')', '{', '}', '[' and ']', determine if the input string is valid.

An input string is valid if:

Open brackets must be closed by the same type of brackets.
Open brackets must be closed in the correct order.
Every close bracket has a corresponding open bracket of the same type.
 
Example 1:

Input: s = "()"

Output: true

Example 2:

Input: s = "()[]{}"

Output: true

Example 3:

Input: s = "(]"

Output: false

Example 4:

Input: s = "([])"

Output: true


Solution: Using stack and hasmap method 

class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        mapping_brackets = {")": "(", "]": "[", "}": "{"}
        for char in s:
            if char in mapping_brackets:
                if stack and stack[-1] == mapping_brackets[char]:  
                    stack.pop() 
                else:
                    return False  
            else:
                stack.append(char)  

        return True if not stack else False


Explanation: 
1. Use a stack to keep track of unmatched opening brackets.
2. When encountering a closing bracket, check if it matches the top of the stack. If it does, remove the matched opening bracket. Otherwise, return False.
3. At the end, if the stack is empty, the brackets are balanced; otherwise, they are not
