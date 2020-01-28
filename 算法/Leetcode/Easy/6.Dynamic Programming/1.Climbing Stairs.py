#!/usr/bin/python
# -*- coding: utf-8 -*-
"""
You are climbing a stair case. It takes n steps to reach to the top.

Each time you can either climb 1 or 2 steps. In how many distinct ways can you climb to the top?

Note: Given n will be a positive integer.

Example 1:

Input: 2
Output: 2
Explanation: There are two ways to climb to the top.
1. 1 step + 1 step
2. 2 steps
Example 2:

Input: 3
Output: 3
Explanation: There are three ways to climb to the top.
1. 1 step + 1 step + 1 step
2. 1 step + 2 steps
3. 2 steps + 1 step
"""


class Solution:
    def climbStairs(self, n: int) -> int:
        result = [1, 2]
        for _ in range(2, n):
            result.append(result[_ - 1] + result[_ - 2])
        return result[n-1]


if __name__ == '__main__':
    a = Solution()
    print(a.climbStairs(3))
    print(a.climbStairs(4))
    print(a.climbStairs(5))
