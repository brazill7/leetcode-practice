""" EASY
For two strings s and t, we say "t divides s" if and only if s = t + t + t + ... + t + t (i.e., t is concatenated with itself one or more times).

Given two strings str1 and str2, return the largest string x such that x divides both str1 and str2.

 

Example 1:

Input: str1 = "ABCABC", str2 = "ABC"
Output: "ABC"

Example 2:

Input: str1 = "ABABAB", str2 = "ABAB"
Output: "AB"

Example 3:

Input: str1 = "LEET", str2 = "CODE"
Output: ""

 

Constraints:

    1 <= str1.length, str2.length <= 1000
    str1 and str2 consist of English uppercase letters.
"""

# Code

class Solution:
    def gcdOfStrings(self, str1: str, str2: str) -> str:
        common_set = set()

        s1_len = len(str1)
        s2_len = len(str2)

        for i in range(max(s1_len, s2_len)):
            j = i + 1

            try:
                check = str1[:j]
                if check == str2[:j]:
                    common_set.add(str(check))
            except: break

        greatest = ""

        for s in common_set:
            count = len(s)

            if count > len(greatest) and s1_len % count == 0 and s2_len % count == 0: 
                s1_rem = int(s1_len / count)
                s2_rem = int(s2_len / count)

                if (s1_rem * s == str1) and (s2_rem * s == str2):                
                    greatest = s

        return greatest

# Test
from _testfunc import testfunc

s = Solution()

testfunc(s.gcdOfStrings, ("ABCABC", "ABC"), "ABC")
testfunc(s.gcdOfStrings, ("ABABAB", "ABAB"), "AB")
testfunc(s.gcdOfStrings, ("LEET", "CODE"), "")
testfunc(s.gcdOfStrings, ("ABCDEF", "ABC"), "")