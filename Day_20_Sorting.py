#!/bin/python3

import sys

n = int(input().strip())
a = list(map(int, input().strip().split(' ')))

swaps_total = 0                     # count the total number of swaps done to sort the list

for i in range(0,len(a)):           # bubble sort: conduct loops for (the num of element) times
    num_of_swaps = 0                # count the number of swaps per one loop
    for j in range(0,len(a)-1):             # one-loop process: comparision of two adjacent elements
        if a[j] > a[j+1]:                   # if the left element is larger than the right element
            a[j], a[j+1] = a[j+1], a[j]     # swap the two adjacent elements
            num_of_swaps += 1
            swaps_total += 1
    if num_of_swaps == 0:           # if all elements are in order (sorted), finish the swapping process
        break

print('Array is sorted in {} swaps.'.format(swaps_total))
print('First Element: {}'.format(a[0]))
print('Last Element: {}'.format(a[len(a)-1]))
