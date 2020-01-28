#!/usr/bin/python
# -*- coding: utf-8 -*-
"""
Given an array containing n distinct numbers taken from 0, 1, 2, ..., n, find the one that is missing from the array.

Example 1:

Input: [3,0,1]
Output: 2
Example 2:

Input: [9,6,4,2,3,5,7,0,1]
Output: 8
Note:
Your algorithm should run in linear runtime complexity. Could you implement it using only constant extra space complexity?
"""
from typing import List


class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        result = int((1 + len(nums)) * len(nums) / 2 - sum(nums))
        return result


if __name__ == '__main__':
    a = Solution()
    print(a.missingNumber([3,0,1]))
    print(a.missingNumber([9,6,4,2,3,5,7,0,1]))
