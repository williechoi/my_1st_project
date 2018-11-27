'''
Hackerrank
Interview preparation Kit: Sherlock and Anagrams
Given a string, find the number of pairs of substrings of the string
that are anagrams of each other

'''



#!/bin/python3

import math
import os
import random
import re
import sys

def sherlockAndAnagrams(s):
    substr = []
    cas = dict()
    total_sum = 0

    for i in range(0, len(s)):
        for j in range(i+1, len(s) + 1):
            substr.append(s[i:j])                   # add all substrings to the list substr

    for each_substr in substr:                      # for each elements in the list substr
        each_substr = ''.join(sorted(each_substr))  # sort the each substring in alphabetical order
        if each_substr not in cas:                  # put the sorted substring into the dict cas
            cas[each_substr] = 1                    # if the sorted substring does not exist in the dict
        else:                                       # create one and assign value 1 to the substring
            cas[each_substr] += 1                   # if it already exists, add 1 to the value

    for k in cas.keys():                            # examine the dict
        p = cas.get(k)
        total_sum += int((p * (p - 1)) / 2)         # compute the combination formula: '# C 2'

    return total_sum                                # return the answer


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    q = int(input())

    for q_itr in range(q):
        s = input()

        result = sherlockAndAnagrams(s)

        fptr.write(str(result) + '\n')

    fptr.close()