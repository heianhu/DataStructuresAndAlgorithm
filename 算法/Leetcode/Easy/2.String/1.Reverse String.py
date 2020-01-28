#!/usr/bin/python
# -*- coding: utf-8 -*-
"""
Write a function that reverses a string. The input string is given as an array of characters char[].

Do not allocate extra space for another array, you must do this by modifying the input array in-place with O(1) extra memory.

You may assume all the characters consist of printable ascii characters.



Example 1:

Input: ["h","e","l","l","o"]
Output: ["o","l","l","e","h"]
Example 2:

Input: ["H","a","n","n","a","h"]
Output: ["h","a","n","n","a","H"]
"""
from typing import List


class Solution:
    def reverseString(self, s: List[str]) -> None:
        """
        Do not return anything, modify s in-place instead.
        """
        for i in range(len(s)//2):
            s[i], s[-i-1] = s[-i-1], s[i]


if __name__ == '__main__':
    test = Solution()
    l = ["h", "e", "l", "l", "o"]
    test.reverseString(l)
    print(l)
    l = ["H", "a", "n", "n", "a", "h"]
    test.reverseString(l)
    print(l)
