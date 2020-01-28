#!/usr/bin/python
# -*- coding: utf-8 -*-
"""
Given a 32-bit signed integer, reverse digits of an integer.

Example 1:

Input: 123
Output: 321
Example 2:

Input: -123
Output: -321
Example 3:

Input: 120
Output: 21
Note:
Assume we are dealing with an environment which could only store integers within the 32-bit signed integer range: [−231,  231 − 1]. For the purpose of this problem, assume that your function returns 0 when the reversed integer overflows.
"""
from typing import List


class Solution:
    def reverse(self, x: int) -> int:
        result = 0
        if x == 0 or not ((-pow(2, 31)) <= x <= (pow(2, 31) - 1)):
            return result
        tag = x // abs(x)
        x = abs(x)
        while x != 0:
            result = (result + x % 10) * 10
            x //= 10
        result //= 10 * tag
        if not ((-pow(2, 31)) <= result <= (pow(2, 31) - 1)):
            return 0
        return result


if __name__ == '__main__':
    test = Solution()
    # print(test.reverse(123))
    print(test.reverse(1534236469))
    print(test.reverse(2147483647))
    # print(test.reverse(0))
