""" EASY

You have a long flowerbed in which some of the plots are planted, and some are not. However, flowers cannot be planted in adjacent plots.

Given an integer array flowerbed containing 0's and 1's, where 0 means empty and 1 means not empty, and an integer n, return true if n new flowers can be planted in the flowerbed without violating the no-adjacent-flowers rule and false otherwise.

 

Example 1:

Input: flowerbed = [1,0,0,0,1], n = 1
Output: true

Example 2:

Input: flowerbed = [1,0,0,0,1], n = 2
Output: false


Constraints:
    1 <= flowerbed.length <= 2 * 104
    flowerbed[i] is 0 or 1.
    There are no two adjacent flowers in flowerbed.
    0 <= n <= flowerbed.length
"""

# Code
from typing import List

class Solution:
    def canPlaceFlowers(self, flowerbed: List[int], n: int) -> bool:
        flowers_left_to_plant = n
        flowerbed_length = len(flowerbed)

        # Check Edge Cases
        if n == 0:
            return True
        if flowerbed_length == 1:
            if flowerbed[0] == 0 and n == 1:
                return True
            else:
                return False
            
        
        # Normal Checks
        for i, plot in enumerate(flowerbed):
            if plot == 1:
                # flower already plotted, ignore
                continue

            if i == 0:
                # only check the next position, since we are at the beginning
                if flowerbed[i+1] == 0:
                    flowers_left_to_plant -= 1
                    flowerbed[i] = 1
            elif i == flowerbed_length - 1:
                # only check the previous position, since we are at the end
                if flowerbed[i-1] == 0:
                    flowers_left_to_plant -= 1
                    flowerbed[i] = 1
            else:
                # check both 
                if flowerbed[i+1] == 0 and flowerbed[i-1] == 0:
                    flowers_left_to_plant -= 1
                    flowerbed[i] = 1
            
            if flowers_left_to_plant == 0:
                break

        return flowers_left_to_plant == 0


# Test

from _testfunc import testfunc

s = Solution()

testfunc(s.canPlaceFlowers, ([1,0,0,0,1], 1), True)
testfunc(s.canPlaceFlowers, ([1,0,0,0,1], 2), False)
testfunc(s.canPlaceFlowers, ([0], 1), True)
testfunc(s.canPlaceFlowers, ([1], 0), True)
