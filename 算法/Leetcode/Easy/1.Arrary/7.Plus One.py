#!/usr/bin/python
# -*- coding: utf-8 -*-
"""
Given a non-empty array of digits representing a non-negative integer, plus one to the integer.

The digits are stored such that the most significant digit is at the head of the list, and each element in the array contain a single digit.

You may assume the integer does not contain any leading zero, except the number 0 itself.

Example 1:

Input: [1,2,3]
Output: [1,2,4]
Explanation: The array represents the integer 123.
Example 2:

Input: [4,3,2,1]
Output: [4,3,2,2]
Explanation: The array represents the integer 4321.
"""
from typing import List


class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        result = list()
        num = 0
        for i in digits:
            num = (num + i) * 10
        num = int(num // 10 + 1)
        while num > 0:
            result.insert(0, num % 10)
            num //= 10

        return result


if __name__ == '__main__':
    test = Solution()
    print(test.plusOne([6, 1, 4, 5, 3, 9, 0, 1, 9, 5, 1, 8, 6, 7, 0, 5, 5, 4, 3]))
    # print(test.plusOne([4, 3, 2, 1]))
