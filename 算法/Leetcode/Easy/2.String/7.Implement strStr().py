#!/usr/bin/python
# -*- coding: utf-8 -*-
"""
Implement strStr().

Return the index of the first occurrence of needle in haystack, or -1 if needle is not part of haystack.

Example 1:

Input: haystack = "hello", needle = "ll"
Output: 2
Example 2:

Input: haystack = "aaaaa", needle = "bba"
Output: -1
Clarification:

What should we return when needle is an empty string? This is a great question to ask during an interview.

For the purpose of this problem, we will return 0 when needle is an empty string. This is consistent to C's strstr() and Java's indexOf().
"""


class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        if not needle:
            return 0
        needle_len = len(needle)
        for index in range(len(haystack)):
            if haystack[index:index+needle_len] == needle:
                return index
        return -1


if __name__ == '__main__':
    test = Solution()
    print(test.strStr('hello', 'll'))
    print(test.strStr('aaaaa', 'bba'))
    print(test.strStr('4193 with words', ''))
