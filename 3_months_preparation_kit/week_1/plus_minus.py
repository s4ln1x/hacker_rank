#!/bin/python3

import math
import os
import random
import re
import sys

# Problem statement:
# Given an array of integers, calculate the ratios of its elements that are positive, negative, and zero. Print the
# decimal value of each fraction on a new line with 6 places after the decimal.

# Complete the 'plusMinus' function below.
#
# The function accepts INTEGER_ARRAY arr as parameter.
#

def plusMinus(arr):
    """

    :param arr:
    :return: None
    """
    positives = [number for number in arr if number > 0]
    negatives = [number for number in arr if number < 0]
    zeroes = [number for number in arr if number == 0]
    arr_length = len(arr)
    print(f'{len(positives)/arr_length:.6f}')
    print(f'{len(negatives)/arr_length:.6f}')
    print(f'{len(zeroes)/arr_length:.6f}')

if __name__ == '__main__':
    n = int(input().strip())

    arr = list(map(int, input().rstrip().split()))

    plusMinus(arr)
