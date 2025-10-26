"""
You are given an integer array height of length n. There are n vertical lines drawn such that the two endpoints of the ith line are (i, 0) and (i, height[i]).

Find two lines that together with the x-axis form a container, such that the container contains the most water.

Return the maximum amount of water a container can store.

Notice that you may not slant the container.

 

Example 1:

Input: height = [1,8,6,2,5,4,8,3,7]
Output: 49
Explanation: The above vertical lines are represented by array [1,8,6,2,5,4,8,3,7]. In this case, the max area of water (blue section) the container can contain is 49.

Example 2:

Input: height = [1,1]
Output: 1

 

Constraints:

    n == height.length
    2 <= n <= 105
    0 <= height[i] <= 104

"""

# Code
from typing import List

class Solution:
    def maxArea(self, height: List[int]) -> int:

        left = 0
        right = len(height) - 1
        max_area = 0

        while left < right:
            # Calculate Area
            width = right - left

            left_height = height[left]
            right_height = height[right]
            lower_height = min(left_height, right_height)

            area = width * lower_height

            if area > max_area: 
                max_area = area

            # Move lower of left or right
            if height[left] > height[right]:
                # Move Right bc left > right
                right -= 1
            else:
                # Move Left bc right > left
                left += 1

        return max_area

# Test

from _testfunc import testfunc

s = Solution()

testfunc(s.maxArea, ([1,8,6,2,5,4,8,3,7], ), 49)
testfunc(s.maxArea, ([1,1], ), 1)