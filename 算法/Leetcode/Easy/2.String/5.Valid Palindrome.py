#!/usr/bin/python
# -*- coding: utf-8 -*-
"""
Given a string, determine if it is a palindrome, considering only alphanumeric characters and ignoring cases.

Note: For the purpose of this problem, we define empty string as valid palindrome.

Example 1:

Input: "A man, a plan, a canal: Panama"
Output: true
Example 2:

Input: "race a car"
Output: false
"""
import re


class Solution:
    def isPalindrome(self, s: str) -> bool:
        s = re.sub('[^\da-zA-Z]', '', s).lower()
        mid = len(s) // 2
        if len(s) % 2:
            if s[:mid] == s[mid+1:][::-1]:
                return True
            else:
                return False
        else:
            if s[:mid] == s[mid:][::-1]:
                return True
            else:
                return False


if __name__ == '__main__':
    test = Solution()
    print(test.isPalindrome('A man, a plan, a canal: Panama'))
    print(test.isPalindrome('race a car'))
    print(test.isPalindrome('rar'))
    print(test.isPalindrome('ra r'))
