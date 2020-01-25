#!/usr/bin/python
# -*- coding: utf-8 -*-
"""
Given an integer, write a function to determine if it is a power of three.

Example 1:

Input: 27
Output: true
Example 2:

Input: 0
Output: false
Example 3:

Input: 9
Output: true
Example 4:

Input: 45
Output: false
Follow up:
Could you do it without using any loop / recursion?
"""


class Solution:
    def isPowerOfThree(self, n: int) -> bool:
        if n < 1:
            return False
        while n > 0:
            if n == 1:
                return True
            if n % 3:
                return False
            n /= 3


if __name__ == '__main__':
    a = Solution()
    print(a.isPowerOfThree(27))
    print(a.isPowerOfThree(0))
    print(a.isPowerOfThree(9))
    print(a.isPowerOfThree(1))

