#!/usr/bin/python
# -*- coding: utf-8 -*-
"""
Given an array nums, write a function to move all 0's to the end of it while maintaining the relative order of the non-zero elements.

Example:

Input: [0,1,0,3,12]
Output: [1,3,12,0,0]
Note:

You must do this in-place without making a copy of the array.
Minimize the total number of operations.
"""
from typing import List


class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        index = 0
        zero_count = 0
        while index + zero_count < len(nums):
            if nums[index] == 0:
                zero_count += 1
                nums.pop(index)
                nums.append(0)
            else:
                index += 1


if __name__ == '__main__':
    test = Solution()
    l = [0, 1, 0, 3, 12]
    test.moveZeroes(l)
    print(l)
    l = [0, 0, 0]
    test.moveZeroes(l)
    print(l)
    l = []
    test.moveZeroes(l)
    print(l)
