'''
Hackerrank: interview preparation kit series - ransom note
This problem intends to check the applicant's ability to use hash tables well
Using hash table, the applicant should figure out whether the second list (note) is a subset of the first list (magazine)
url: https://www.hackerrank.com/challenges/ctci-ransom-note/problem?h_l=interview&playlist_slugs%5B%5D=interview-preparation-kit&playlist_slugs%5B%5D=dictionaries-hashmaps

'''



#!/bin/python3

import math
import os
import random
import re
import sys


def checkMagazine(magazine, note):          # a function that checks if the list 'note' is a subset of the list 'magazine'
    d_note = dict()                         # define a dict type in order to use hash table
    isPerfectRansomNote = 'Yes'             # the target value: whether or not note is a subset of magazine
    for each_word in note:                  # plug in each element into the dict in the form of {element : frequency}
        if each_word not in d_note:         # if the element is not included in the dict key
            d_note[each_word] = 1           # create one, and assign the value of 1
        else:                               # if the element already exists in the dict key
            d_note[each_word] += 1          # add 1 to the value

    for each_word_2 in magazine:            # examine the elements of the list 'magazine'
        if each_word_2 in d_note:           # if an element exists as the dict key
            if d_note[each_word_2] > 0:
                d_note[each_word_2] -= 1    # reduce its frequency by 1

    for i in d_note.keys():
        if d_note[i] != 0:                  # not every dict value is 0: 'note' is not a subset of 'magazine'
            isPerfectRansomNote = 'No'
            break

    print(isPerfectRansomNote)



if __name__ == '__main__':
    mn = input().split()

    m = int(mn[0])

    n = int(mn[1])

    magazine = input().rstrip().split()

    note = input().rstrip().split()

    checkMagazine(magazine, note)
