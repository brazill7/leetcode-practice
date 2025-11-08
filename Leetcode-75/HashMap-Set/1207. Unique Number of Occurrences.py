""" EASY
Given an array of integers arr, return true if the number of occurrences of each value in the array is unique or false otherwise.


Example 1:

Input: arr = [1,2,2,1,1,3]
Output: true
Explanation: The value 1 has 3 occurrences, 2 has 2 and 3 has 1. No two values have the same number of occurrences.

Example 2:

Input: arr = [1,2]
Output: false

Example 3:

Input: arr = [-3,0,1,-3,1,1,1,-3,10,0]
Output: true
"""
from sympy import false


# Code
from typing import List

class Solution:
    def uniqueOccurrences(self, arr: List[int]) -> bool:
        occurrences = dict()

        for num in arr:
            if num not in occurrences:
                occurrences[num] = 1
            else:
                occurrences[num] += 1

        values = occurrences.values()

        return len(values) == len(set(values))

# Test

from _testfunc import testfunc

s = Solution()


testfunc(s.uniqueOccurrences, ([1,2,2,1,1,3], ), True)
testfunc(s.uniqueOccurrences, ([1,2], ), False)
testfunc(s.uniqueOccurrences, ([-3,0,1,-3,1,1,1,-3,10,0], ), True)