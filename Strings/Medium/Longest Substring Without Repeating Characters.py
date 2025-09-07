Given a string s, find the length of the longest substring without duplicate characters.

Example 1:

Input: s = "abcabcbb"
Output: 3
Explanation: The answer is "abc", with the length of 3.
Example 2:

Input: s = "bbbbb"
Output: 1
Explanation: The answer is "b", with the length of 1.
Example 3:

Input: s = "pwwkew"
Output: 3
Explanation: The answer is "wke", with the length of 3.
Notice that the answer must be a substring, "pwke" is a subsequence and not a substring.

Solution: Using Two pointer approach

class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        n = len(s)
        seen = set()
        left = 0
        right = 0
        max_len = 0

        while right < n: 
            if s[right] not in seen:
                seen.add(s[right])
                max_len = max(max_len, right - left + 1)
                right += 1
            else:
                seen.remove(s[left])
                left += 1
        return max_len

Exaplanation: 
###  Approach: Sliding Window with Set

We use a sliding window** approach to keep track of the current substring without duplicates.

- A `left` pointer represents the start of the current window.
- A `right` pointer expands the window one character at a time.
- A `set` named `seen` stores characters currently in the window.
- If `s[right]` is not in `seen`, we add it and update the max length.
- If it is a duplicate**, we shrink the window from the `left` until the duplicate is removed.

This ensures that at any point, the window contains only unique characters.
