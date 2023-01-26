#!/bin/python3

import math
import os
import random
import re
import sys

# Problem Statement:
# Given five positive integers, find the minimum and maximum values that can be calculated by summing exactly four of the
# five integers. Then print the respective minimum and maximum values as a single line of two space-separated long
# integers.

#
# Complete the 'miniMaxSum' function below.
#
# The function accepts INTEGER_ARRAY arr as parameter.
#

def miniMaxSum(arr):
    arr_minimum = sorted(arr)
    arr_maximum = sorted(arr, reverse=True)
    print(sum(arr_minimum[:4]), sum(arr_maximum[:4]))

if __name__ == '__main__':

    arr = list(map(int, input().rstrip().split()))
    # arr = [1, 2, 3, 4, 5]
    miniMaxSum(arr)
