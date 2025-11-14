"""
You have a set of integers s, which originally contains all the numbers from 1 to n. Unfortunately, due to some error, one of the numbers in s got duplicated to another number in the set, which results in repetition of one number and loss of another number.

You are given an integer array nums representing the data status of this set after the error.

Find the number that occurs twice and the number that is missing and return them in the form of an array.

Example 1:
Input: nums = [1,2,2,4]
Output: [2,3]

Example 2:
Input: nums = [1,1]
Output: [1,2]
"""

# Code

from typing import List

class Solution:
    def findErrorNums(self, nums: List[int]) -> List[int]:
        seen = set()
        duplicate = -1

        # Find the duplicate
        for num in nums:
            if num in seen:
                duplicate = num
            else:
                seen.add(num)

        # Missing number = the one not in seen
        n = len(nums)
        for i in range(1, n + 1):
            if i not in seen:
                missing = i
                break

        return [duplicate, missing]

# Test

from _testfunc import testfunc

s = Solution()


testfunc(s.findErrorNums, ([1,2,2,4], ), [2,3])
testfunc(s.findErrorNums, ([1,1], ), [1,2])
testfunc(s.findErrorNums, ([1,2,3,4,5,5], ), [5,6])
testfunc(s.findErrorNums, ([1,1,3,4,5], ), [1,2])