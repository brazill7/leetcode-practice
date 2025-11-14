"""

"""

# Code

from typing import List

class Solution:
    def shuffle(self, nums: List[int], n: int) -> List[int]:
        shuffled_array = []
        i = 0

        while n < len(nums):
            shuffled_array.append(nums[i])
            shuffled_array.append(nums[n])

            i += 1
            n += 1
        return shuffled_array

# Test

from _testfunc import testfunc

s = Solution()


testfunc(s.shuffle, ([2,5,1,3,4,7], 3), [2,3,5,4,1,7])
testfunc(s.shuffle, ([1,2,3,4,4,3,2,1], 4), [1,4,2,3,3,2,4,1])
testfunc(s.shuffle, ([1,1,2,2], 2), [1,2,1,2])