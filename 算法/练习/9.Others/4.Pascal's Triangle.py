#!/usr/bin/python
# -*- coding: utf-8 -*-
"""
Given a non-negative integer numRows, generate the first numRows of Pascal's triangle.


In Pascal's triangle, each number is the sum of the two numbers directly above it.

Example:

Input: 5
Output:
[
     [1],
    [1,1],
   [1,2,1],
  [1,3,3,1],
 [1,4,6,4,1]
]
"""
from typing import List


class Solution:
    def generate(self, numRows: int) -> List[List[int]]:
        result = [
            [1],
            [1, 1]
        ]
        if numRows < 3:
            return result[:numRows]
        for _ in range(numRows - 2):
            tmp = [
                result[-1][index] + result[-1][index - 1]
                for index in range(1, len(result[-1]))
            ]
            tmp.insert(0, 1)
            tmp.append(1)
            result.append(tmp)
        return result


if __name__ == '__main__':
    a = Solution()
    print(a.generate(1))
    print(a.generate(2))
    print(a.generate(5))
