Given a positive integer n, write a function that returns the number of set bits in its binary representation (also known as the Hamming weight).

Example 1:

Input: n = 11

Output: 3

Explanation:

The input binary string 1011 has a total of three set bits.

Example 2:

Input: n = 128

Output: 1

Explanation:

The input binary string 10000000 has a total of one set bit.

Example 3:

Input: n = 2147483645

Output: 30

Explanation:

The input binary string 1111111111111111111111111111101 has a total of thirty set bits.

Constraints:

1 <= n <= 231 - 1

Solution: Using Brian Kernighan’s Algorithm

class Solution:
    def hammingWeight(self, n: int) -> int:
        count = 0
        while n:
            n &= n - 1
            count += 1
        return count

Explanation: 
# 1.Initialize count = 0.
# 2. While n > 0:
# 3. Do n = n & (n - 1) → removes the rightmost set bit.
# 4. Increment count.
# 5. Return count.
# Time Complexity: O(k) → where k is the number of set bits (not the total number of bits).
# Space Complexity: O(1).

