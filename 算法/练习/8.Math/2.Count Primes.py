#!/usr/bin/python
# -*- coding: utf-8 -*-
"""
Count the number of prime numbers less than a non-negative number, n.

Example:

Input: 10
Output: 4
Explanation: There are 4 prime numbers less than 10, they are 2, 3, 5, 7.
"""
from math import sqrt, floor


class Solution:
    def isPrimes(self, n: int) -> bool:
        for i in range(2, floor(sqrt(n)) + 1):
            if not n % i:
                return False
        return True

    def countPrimes(self, n: int) -> int:
        result = 0
        primes = [True] * n

        for i in range(2, n):
            if primes[i]:
                result += 1
                j = 2
                while i * j < n:
                    primes[i * j] = False
                    j += 1
        return result


if __name__ == '__main__':
    a = Solution()
    print(a.countPrimes(2))
    print(a.countPrimes(10))
    print(a.countPrimes(999983))
