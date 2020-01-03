#!/usr/bin/env python3
# -*- coding: utf-8 -*-
__author__ = 'heianhu'
import itertools
permutations_set = set()

def Permutation(string_list: list, n: int):
    if n == len(string_list) - 1:
        permutations_set.add(''.join(string_list))
        # print(''.join(string_list))
    else:
        for i in range(n, len(string_list)):
            string_list[i], string_list[n] = string_list[n], string_list[i]
            Permutation(string_list, n + 1)
            string_list[i], string_list[n] = string_list[n], string_list[i]


if __name__ == '__main__':
    string = 'ABCC'
    Permutation(list(string), 0)
    for i in permutations_set:
        print(i)
    print(len(permutations_set))

    permutations = list(itertools.permutations(string))
    for i in permutations:
        print(''.join(i))
    print(len(permutations))
