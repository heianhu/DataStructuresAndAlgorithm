#!/usr/bin/python
# -*- coding: utf-8 -*-
"""
Given a string, find the first non-repeating character in it and return it's index. If it doesn't exist, return -1.

Examples:

s = "leetcode"
return 0.

s = "loveleetcode",
return 2.
Note: You may assume the string contain only lowercase letters.
"""


class Solution:
    def firstUniqChar(self, s: str) -> int:
        for index in range(len(s)):
            # print(s[index], s[index + 1:])
            if s[index] not in s[0:index] + s[index + 1:]:
                return index
        return -1


if __name__ == '__main__':
    test = Solution()
    # print(test.firstUniqChar('leetcode'))
    # print(test.firstUniqChar('loveleetcode'))
    # print(test.firstUniqChar(''))
    # print(test.firstUniqChar('l'))
    print(test.firstUniqChar('cc'))
    print(test.firstUniqChar('eea'))
