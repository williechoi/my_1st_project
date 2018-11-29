'''
Hackerrank: interview preparation kit series: Count triplets
This program intends to check the applicant's ability to use hashmaps ingeniously
url: https://www.hackerrank.com/challenges/count-triplets-1/problem?h_l=interview&playlist_slugs%5B%5D=interview-preparation-kit&playlist_slugs%5B%5D=dictionaries-hashmaps

'''


import os
from collections import defaultdict


def countTriplets(arr, r):                  # a function that counts how many triplets can be made from the list
    dict_r2 = defaultdict(int)              # candidates for the 2nd part of the triplet
    dict_r3 = defaultdict(int)              # candidates for the 3rd part of the triplet
    cnt = 0                                 # target value: count
    for i in arr:
        dict_r2[i * r] += 1                 # i*r is needed (for the 2nd part of the triplet)
        if i in dict_r2:                    # if i belongs to the 2nd part of the triplet
            dict_r3[i * r] += dict_r2[i]    # i*r is needed (for the 3rd part of the triplet)
        if i in dict_r3:                    # if i belongs to the 3rd part of triplet
            cnt += dict_r3[i]               # triplets can be made! so add up the value to the count

    return cnt


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    nr = input().rstrip().split()

    n = int(nr[0])

    r = int(nr[1])

    arr = list(map(int, input().rstrip().split()))

    ans = countTriplets(arr, r)

    fptr.write(str(ans) + '\n')

    fptr.close()