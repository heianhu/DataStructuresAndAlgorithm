#!/usr/bin/python
# -*- coding: utf-8 -*-
"""
Shuffle a set of numbers without duplicates.

Example:

// Init an array with set 1, 2, and 3.
int[] nums = {1,2,3};
Solution solution = new Solution(nums);

// Shuffle the array [1,2,3] and return its result. Any permutation of [1,2,3] must equally likely to be returned.
solution.shuffle();

// Resets the array back to its original configuration [1,2,3].
solution.reset();

// Returns the random shuffling of array [1,2,3].
solution.shuffle();
"""
from typing import List
import random

class Solution:

    def __init__(self, nums: List[int]):
        self.rlist = nums

    def reset(self) -> List[int]:
        """
        Resets the array to its original configuration and return it.
        """
        return self.rlist

    def shuffle(self) -> List[int]:
        """
        Returns a random shuffling of the array.
        """
        tmp = self.rlist.copy()
        random.shuffle(tmp)
        return tmp

# Your Solution object will be instantiated and called as such:
# obj = Solution(nums)
# param_1 = obj.reset()
# param_2 = obj.shuffle()

if __name__ == '__main__':
    nums = [1, 2, 3]
    obj = Solution(nums)
    print(obj.reset())
    print(obj.shuffle())
    print(obj.reset())
