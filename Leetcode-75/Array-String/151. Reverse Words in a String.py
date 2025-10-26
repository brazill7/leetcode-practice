""" MEDIUM
Given an input string s, reverse the order of the words.

A word is defined as a sequence of non-space characters. The words in s will be separated by at least one space.

Return a string of the words in reverse order concatenated by a single space.

Note that s may contain leading or trailing spaces or multiple spaces between two words. The returned string should only have a single space separating the words. Do not include any extra spaces.


Example 1:

Input: s = "the sky is blue"
Output: "blue is sky the"

Example 2:

Input: s = "  hello world  "
Output: "world hello"
Explanation: Your reversed string should not contain leading or trailing spaces.

Example 3:

Input: s = "a good   example"
Output: "example good a"
Explanation: You need to reduce multiple spaces between two words to a single space in the reversed string.


Constraints:

    1 <= s.length <= 104
    s contains English letters (upper-case and lower-case), digits, and spaces ' '.
    There is at least one word in s.

 

Follow-up: If the string data type is mutable in your language, can you solve it in-place with O(1) extra space?

"""

# Code

class Solution:
    def reverseWords(self, s: str) -> str:   
        word_hs = {}
        j = 0

        for i, c in enumerate(s):
            if i == 0 and c != ' ':
                word_hs[j] = c
                continue
            if c == ' ':
                continue
            
            if s[i-1] == ' ':
                # make new word
                j += 1 
                word_hs[j] = c
            else:
                # append to old word
                word_hs[j] += c
                
        values = list(word_hs.values())
        values.reverse()

        return ' '.join(values)
       

# Test

from _testfunc import testfunc

s = Solution()

testfunc(s.reverseWords, ("the sky is blue", ), "blue is sky the")
testfunc(s.reverseWords, ("  hello world  ", ), "world hello")
testfunc(s.reverseWords, ("a good   example", ), "example good a")
testfunc(s.reverseWords, ("good", ), "good")