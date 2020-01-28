#!/usr/bin/python
# -*- coding: utf-8 -*-
"""
Write a function to find the longest common prefix string amongst an array of strings.

If there is no common prefix, return an empty string "".

Example 1:

Input: ["flower","flow","flight"]
Output: "fl"
Example 2:

Input: ["dog","racecar","car"]
Output: ""
Explanation: There is no common prefix among the input strings.
Note:

All given inputs are in lowercase letters a-z.
"""
from typing import List


class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        if not strs:
            return ''
        result = strs[0]
        for current_str in strs:
            for result_index in range(len(result), 0, -1):
                if result[:result_index] == current_str[:result_index]:
                    result = result[:result_index]
                    break
            else:
                result = ''
                break
        return result


if __name__ == '__main__':
    test = Solution()
    print(test.longestCommonPrefix(["flower","flow","flight"]))
    print(test.longestCommonPrefix(["dog","racecar","car"]))
    print(test.longestCommonPrefix([]))
    print(test.longestCommonPrefix(['a']))
    print(test.longestCommonPrefix(['c', 'c']))
    print(test.longestCommonPrefix(["c","acc","ccc"]))
