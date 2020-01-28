#!/usr/bin/python
# -*- coding: utf-8 -*-
"""
Given two strings s and t , write a function to determine if t is an anagram of s.

Example 1:

Input: s = "anagram", t = "nagaram"
Output: true
Example 2:

Input: s = "rat", t = "car"
Output: false
Note:
You may assume the string contains only lowercase alphabets.

Follow up:
What if the inputs contain unicode characters? How would you adapt your solution to such case?
"""


class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        try:
            s = s.encode('ascii')
            t = t.encode('ascii')
        except Exception:
            return False
        if len(s) != len(t):
            return False
        t = list(t)
        for i in s:
            if i in t:
                t.pop(t.index(i))
            else:
                return False
        return True


if __name__ == '__main__':
    test = Solution()
    print(test.isAnagram('anagram', 'nagaram'))
    print(test.isAnagram('rat', 'car'))
