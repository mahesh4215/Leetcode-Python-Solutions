Given two strings s and t, return true if t is an anagram of s, and false otherwise.

Example 1:

Input: s = "anagram", t = "nagaram"

Output: true

Example 2:

Input: s = "rat", t = "car"

Output: false

Constraints:

1 <= s.length, t.length <= 5 * 104
s and t consist of lowercase English letters.

Solution 1: Using character frequency count 

class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return false
        count_s = {}
        count_t = {}

        for char in s:
            count_s[char] = count_s.get(char, 0) + 1
        for char in t:
            count_t[char] = count_t.get(char, 0) + 1

        return count_s == count_t 

Solution 2: Using sorting 
  class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
      return sorted(s) == sorted(t)

Solution 3: Using counter() method 

  class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
      return Counter(s) == Counter(t)
