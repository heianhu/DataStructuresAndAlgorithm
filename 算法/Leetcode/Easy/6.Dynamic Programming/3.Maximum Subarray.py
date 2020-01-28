#!/usr/bin/python
# -*- coding: utf-8 -*-
"""
Given an integer array nums, find the contiguous subarray (containing at least one number) which has the largest sum and return its sum.

Example:

Input: [-2,1,-3,4,-1,2,1,-5,4],
Output: 6
Explanation: [4,-1,2,1] has the largest sum = 6.
Follow up:

If you have figured out the O(n) solution, try coding another solution using the divide and conquer approach, which is more subtle.
"""
from typing import List


class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        result = -1 << 31
        current_sum = 0
        for num in nums:
            current_sum = max(current_sum + num, num)
            result = max(result, current_sum)
        return result

    # def maxSubArray(self, nums: List[int]) -> int:
    #     if len(nums) == 1:
    #         return nums[0]
    #     if not nums:
    #         return 0
    #     mid = nums[len(nums)//2]
    #     left = self.maxSubArray(nums[:len(nums)//2])
    #     right = self.maxSubArray(nums[len(nums)//2+1:])
    #     left_max = max([mid, left, left + mid])
    #     right_max = max([mid, right, right + mid])
    #     print(nums, nums[len(nums)//2], max(left_max, right_max))
    #     return max(left_max, right_max)


if __name__ == '__main__':
    a = Solution()
    print(a.maxSubArray([-2,1,-3,4,-1,2,1,-5,4]))
