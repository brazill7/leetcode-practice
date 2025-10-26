""" MEDIUM
Given an integer array nums, return true if there exists a triple of indices (i, j, k) such that i < j < k and nums[i] < nums[j] < nums[k]. If no such indices exists, return false.

 

Example 1:

Input: nums = [1,2,3,4,5]
Output: true
Explanation: Any triplet where i < j < k is valid.

Example 2:

Input: nums = [5,4,3,2,1]
Output: false
Explanation: No triplet exists.

Example 3:

Input: nums = [2,1,5,0,4,6]
Output: true
Explanation: One of the valid triplet is (3, 4, 5), because nums[3] == 0 < nums[4] == 4 < nums[5] == 6.


Constraints:
    1 <= nums.length <= 5 * 105
    -231 <= nums[i] <= 231 - 1

 
Follow up: Could you implement a solution that runs in O(n) time complexity and O(1) space complexity?
"""

# Code
from typing import List

class Solution:
    def increasingTriplet(self, nums: List[int]) -> bool:
        min1 = float('inf')
        min2 = float('inf')

        for n in nums:
            if n <= min1:
                min1 = n
            elif n <= min2:
                min2 = n  
            else:
                return True  
        return False  
# Test

from _testfunc import testfunc

s = Solution()

testfunc(s.increasingTriplet, ([1,2,3,4,5], ), True)
testfunc(s.increasingTriplet, ([5,4,3,2,1], ), False)
testfunc(s.increasingTriplet, ([2,1,5,0,4,6], ), True)
testfunc(s.increasingTriplet, ([20,100,10,12,5,13], ), True)
testfunc(s.increasingTriplet, ([1,5,0,4,1,3], ), True)

