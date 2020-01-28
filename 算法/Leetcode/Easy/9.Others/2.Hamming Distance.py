#!/usr/bin/python
# -*- coding: utf-8 -*-
"""
The Hamming distance between two integers is the number of positions at which the corresponding bits are different.

Given two integers x and y, calculate the Hamming distance.

Note:
0 ≤ x, y < 231.

Example:

Input: x = 1, y = 4

Output: 2

Explanation:
1   (0 0 0 1)
4   (0 1 0 0)
       ↑   ↑

The above arrows point to positions where the corresponding bits are different.
"""


class Solution:
    def hammingDistance(self, x: int, y: int) -> int:
        result = x ^ y
        count = 0
        while result != 0 and result != -1:
            if result % 2:
                count += 1
            result >>= 1
        if result == -1:
            count = 32 - count + 1
        return count


if __name__ == '__main__':
    a = Solution()
    print(a.hammingDistance(-1, 4))
    # print(a.hammingDistance(-1, -4))
    # print(a.hammingDistance(1, 4))



