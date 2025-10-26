"""
Given an integer array nums, move all 0's to the end of it while maintaining the relative order of the non-zero elements.

Note that you must do this in-place without making a copy of the array.

 

Example 1:

Input: nums = [0,1,0,3,12]
Output: [1,3,12,0,0]

Example 2:

Input: nums = [0]
Output: [0]

Constraints:

    1 <= nums.length <= 104
    -231 <= nums[i] <= 231 - 1
"""

# Code

from typing import List

class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """

        left = 0
        for right in range(len(nums)):
            if nums[right] != 0:
                nums[left], nums[right] = nums[right], nums[left]
                left += 1

        

                

        

# Test

from _testfunc import testfunc

s = Solution()

a = [0,1,0,3,12]
s.moveZeroes(a)
assert a == [1,3,12,0,0], f"expected \"[1,3,12,0,0]\" got {a}"

a = [0]
s.moveZeroes(a)
assert a == [0], f"expected \"[0]\" got {a}"


a = [5, 4, 0, 3, 0, 5, 9, 0, 0]
s.moveZeroes(a)
assert a == [5,4,3,5,9,0,0,0,0], f"expected \"[5,4,3,5,9,0,0,0,0]\" got {a}"