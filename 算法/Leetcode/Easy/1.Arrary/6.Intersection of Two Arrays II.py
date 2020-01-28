#!/usr/bin/python
# -*- coding: utf-8 -*-
"""
Given two arrays, write a function to compute their intersection.

Example 1:

Input: nums1 = [1,2,2,1], nums2 = [2,2]
Output: [2,2]
Example 2:

Input: nums1 = [4,9,5], nums2 = [9,4,9,8,4]
Output: [4,9]
Note:

Each element in the result should appear as many times as it shows in both arrays.
The result can be in any order.
Follow up:

What if the given array is already sorted? How would you optimize your algorithm?
What if nums1's size is small compared to nums2's size? Which algorithm is better?
What if elements of nums2 are stored on disk, and the memory is limited such that you cannot load all elements into the memory at once?
"""
from typing import List


class Solution:
    def intersect(self, nums1: List[int], nums2: List[int]) -> List[int]:
        result = list()
        tmp_dic = dict()
        for i in nums1:
            if i not in tmp_dic:
                tmp_dic[i] = 0
            tmp_dic[i] += 1
        for i in nums2:
            if tmp_dic.get(i, 0) > 0:
                result.append(i)
                tmp_dic[i] -= 1
        return result


if __name__ == '__main__':
    test = Solution()
    print(test.intersect([1, 2, 2, 1], [2, 2]))
    print(test.intersect([4, 9, 5], [9, 4, 9, 8, 4]))
