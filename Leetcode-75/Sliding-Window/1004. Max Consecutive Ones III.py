""" MEDIUM
Given a binary array nums and an integer k, return the maximum number of consecutive 1's in the array if you can flip at most k 0's.

Example 1:
Input: nums = [1,1,1,0,0,0,1,1,1,1,0], k = 2
Output: 6
Explanation: [1,1,1,0,0,1,1,1,1,1,1]
Bolded numbers were flipped from 0 to 1. The longest subarray is underlined.

Example 2:
Input: nums = [0,0,1,1,0,0,1,1,1,0,1,1,0,0,0,1,1,1,1], k = 3
Output: 10
Explanation: [0,0,1,1,1,1,1,1,1,1,1,1,0,0,0,1,1,1,1]
Bolded numbers were flipped from 0 to 1. The longest subarray is underlined.
"""

"""
    
"""

# Code

from typing import List

from typing import List

class Solution:
    def longestOnes(self, nums: List[int], k: int) -> int:
        j = zeros = longest = 0


        for i in range(len(nums)):
            if nums[i] == 0:
                zeros += 1

            while zeros > k:
                if nums[j] == 0:
                    zeros -= 1
                j += 1

            longest = max(longest, i - j + 1)

        return longest



# Test

from _testfunc import testfunc

s = Solution()


testfunc(s.longestOnes, ([1,1,1,0,0,0,1,1,1,1,0], 2), 6)
testfunc(s.longestOnes, ([0,0,1,1,0,0,1,1,1,0,1,1,0,0,0,1,1,1,1], 3), 10)

# Edge cases
testfunc(s.longestOnes, ([], 2), 0)  # Empty array
testfunc(s.longestOnes, ([1], 0), 1)  # Single 1, no flips
testfunc(s.longestOnes, ([0], 1), 1)  # Single 0, one flip allowed
testfunc(s.longestOnes, ([0], 0), 0)  # Single 0, no flips allowed

# Small arrays
testfunc(s.longestOnes, ([1,0,1], 1), 3)  # Flip the middle 0
testfunc(s.longestOnes, ([1,0,0,1], 1), 2)  # Flip one zero
testfunc(s.longestOnes, ([1,0,0,1], 2), 4)  # Flip both zeros

# Alternating pattern
testfunc(s.longestOnes, ([0,1,0,1,0,1,0], 2), 5)  # Flip two zeros → [0,1,1,1,1,1,0]
testfunc(s.longestOnes, ([1,0,1,0,1,0,1], 3), 7)  # Flip all zeros → full length

# All zeros
testfunc(s.longestOnes, ([0,0,0,0,0], 2), 2)  # Flip any two
testfunc(s.longestOnes, ([0,0,0,0,0], 5), 5)  # Flip all

# All ones
testfunc(s.longestOnes, ([1,1,1,1,1], 2), 5)  # Nothing to flip

# Large blocks of ones/zeros
testfunc(s.longestOnes, ([1,1,0,0,1,1,1,0,1,1,0,1,1,1,1], 2), 11)
testfunc(s.longestOnes, ([1,1,0,0,1,1,1,0,1,1,0,1,1,0,1], 3), 11)

# Flip capacity larger than zeros count
testfunc(s.longestOnes, ([1,0,1,0,1], 10), 5)  # Can flip all zeros easily

# No flips allowed
testfunc(s.longestOnes, ([1,1,0,1,1,1,0,1], 0), 3)  # Longest run of 1s only

# Stress test (pattern)
testfunc(s.longestOnes, ([1,0]*50, 10), 21)  # Flip 10 zeros → 21 ones total

