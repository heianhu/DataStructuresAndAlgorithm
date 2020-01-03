#!/usr/bin/python
# -*- coding: utf-8 -*-
"""
Given an array of integers, return indices of the two numbers such that they add up to a specific target.

You may assume that each input would have exactly one solution, and you may not use the same element twice.

Example:

Given nums = [2, 7, 11, 15], target = 9,

Because nums[0] + nums[1] = 2 + 7 = 9,
return [0, 1].
"""
from typing import List


class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        for index in range(len(nums)):
            if target - nums[index] in nums[index + 1:]:
                return [index, index + nums[index + 1:].index(target - nums[index]) + 1]
        return [None, None]


if __name__ == '__main__':
    test = Solution()
    print(test.twoSum([2, 7, 11, 15], 9))
