""" EASY
Given a string s, reverse only all the vowels in the string and return it.

The vowels are 'a', 'e', 'i', 'o', and 'u', and they can appear in both lower and upper cases, more than once.

 

Example 1:

Input: s = "IceCreAm"

Output: "AceCreIm"

Explanation:

The vowels in s are ['I', 'e', 'e', 'A']. On reversing the vowels, s becomes "AceCreIm".

Example 2:

Input: s = "leetcode"

Output: "leotcede"

Constraints:

    1 <= s.length <= 3 * 105
    s consist of printable ASCII characters.


"""

# Code

class Solution:
    def reverseVowels(self, s: str) -> str:
        string_length = len(s)

        # Edge Case
        if string_length == 1:  return s

        # Normal Cases
        vowels = "AEIOUaeiou"
        s_list = list(s)

        vowel_indexes = [ i for i, c in enumerate(s_list) 
                         if c in vowels ]
        
        left, right = 0, (len(vowel_indexes) - 1)

        while left < right:
            i, j = vowel_indexes[left], vowel_indexes[right]
            s_list[i], s_list[j] = s_list[j], s_list[i]

            left += 1
            right -= 1

        return ''.join(s_list)



# Test

from _testfunc import testfunc

s = Solution()

testfunc(s.reverseVowels, ("leetcode", ), "leotcede")
testfunc(s.reverseVowels, ("IceCreAm", ), "AceCreIm")
testfunc(s.reverseVowels, ("I", ), "I")
testfunc(s.reverseVowels, ("C", ), "C")
testfunc(s.reverseVowels, ("IC", ), "IC")
testfunc(s.reverseVowels, ("AE", ), "EA")