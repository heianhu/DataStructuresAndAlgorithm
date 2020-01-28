#!/usr/bin/python
# -*- coding: utf-8 -*-
"""
Given two sorted integer arrays nums1 and nums2, merge nums2 into nums1 as one sorted array.

Note:

The number of elements initialized in nums1 and nums2 are m and n respectively.
You may assume that nums1 has enough space (size that is greater or equal to m + n) to hold additional elements from nums2.
Example:

Input:
nums1 = [1,2,3,0,0,0], m = 3
nums2 = [2,5,6],       n = 3

Output: [1,2,2,3,5,6]
"""
from typing import List


class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        """
        p1 = 0
        p2 = 0
        while p1 < m and p2 < n and nums2:
            if nums1[p1+p2] >= nums2[0]:
                nums1.insert(p1+p2, nums2.pop(0))
                p2 += 1
            else:
                p1 += 1
        if nums2:
            while nums2:
                nums1.insert(p1+p2, nums2.pop(0))
                p2 += 1
        nums1[::] = nums1[:m + n]


if __name__ == '__main__':
    n1 = [4,0,0,0,0,0]
    m = 1
    n2 = [1,2,3,5,6]
    n = 5
    Solution().merge(n1, m, n2, n)
    print(n1, n2)
    n1 = [0]
    m = 0
    n2 = [1]
    n = 1
    Solution().merge(n1, m, n2, n)
    print(n1, n2)
