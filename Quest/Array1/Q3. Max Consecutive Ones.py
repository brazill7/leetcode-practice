"""
Given a binary array nums, return the maximum number of consecutive 1's in the array.

Example 1:

Input: nums = [1,1,0,1,1,1]
Output: 3
Explanation: The first two digits or the last three digits are consecutive 1s. The maximum number of consecutive 1s is 3.

Example 2:

Input: nums = [1,0,1,1,0,1]
Output: 2

"""

# Code

from typing import List

class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
        maxConsecutiveOnes = 0
        currentConsecutiveOnes = 0
        i = 0

        while i < len(nums):
            if nums[i] == 1:
                currentConsecutiveOnes += 1
            else:
                currentConsecutiveOnes = 0

            maxConsecutiveOnes = max(maxConsecutiveOnes, currentConsecutiveOnes)

            i += 1
        return maxConsecutiveOnes

# Test

from _testfunc import testfunc

s = Solution()


testfunc(s.findMaxConsecutiveOnes, ([1,1,0,1,1,1], ), 3)
testfunc(s.findMaxConsecutiveOnes, ([1,0,1,1,0,1], ), 2)