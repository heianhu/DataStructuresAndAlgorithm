#!/usr/bin/python
# -*- coding: utf-8 -*-
"""
You are a professional robber planning to rob houses along a street. Each house has a certain amount of money stashed, the only constraint stopping you from robbing each of them is that adjacent houses have security system connected and it will automatically contact the police if two adjacent houses were broken into on the same night.

Given a list of non-negative integers representing the amount of money of each house, determine the maximum amount of money you can rob tonight without alerting the police.

Example 1:

Input: [1,2,3,1]
Output: 4
Explanation: Rob house 1 (money = 1) and then rob house 3 (money = 3).
             Total amount you can rob = 1 + 3 = 4.
Example 2:

Input: [2,7,9,3,1]
Output: 12
Explanation: Rob house 1 (money = 2), rob house 3 (money = 9) and rob house 5 (money = 1).
             Total amount you can rob = 2 + 9 + 1 = 12.

[2,7,9,3,1,2]
13

[1,2,7,9,3,1]
12
"""
from typing import List


class Solution:
    def rob(self, nums: List[int]) -> int:
        if not nums:
            return 0
        elif len(nums) <= 2:
            return max(nums[0], nums[-1])
        else:
            result = [nums[0], max(nums[0], nums[1])]
            for index in range(2, len(nums)):
                result.append(max(result[index - 1], result[index - 2] + nums[index]))
            return result[-1]


if __name__ == '__main__':
    a = Solution()
    print(a.rob([1, 2, 7, 9, 3, 1]))
    print(a.rob([2, 7, 9, 3, 1, 2]))
    print(a.rob([2, 7, 9, 3, 1]))
    print(a.rob([1, 2, 3, 1]))
