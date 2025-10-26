""" MEDIUM
Given a string s and an integer k, return the maximum number of vowel letters in any substring of s with length k.

Vowel letters in English are 'a', 'e', 'i', 'o', and 'u'.



Example 1:

Input: s = "abciiidef", k = 3
Output: 3
Explanation: The substring "iii" contains 3 vowel letters.

Example 2:

Input: s = "aeiou", k = 2
Output: 2
Explanation: Any substring of length 2 contains 2 vowels.

Example 3:

Input: s = "leetcode", k = 3
Output: 2
Explanation: "lee", "eet" and "ode" contain 2 vowels.



Constraints:

    1 <= s.length <= 105
    s consists of lowercase English letters.
    1 <= k <= s.length


"""

# Code

class Solution:
    def maxVowels(self, s: str, k: int) -> int:
        vowels = set('aeiou')
        current_count = 0
        max_count = 0

        for i in range(k):
            if s[i] in vowels:
                current_count += 1
        max_count = current_count

        for i in range(k, len(s)):
            if s[i - k] in vowels:
                current_count -= 1
            if s[i] in vowels:
                current_count += 1

            max_count = max(max_count, current_count)

            if max_count == k:
                return k

        return max_count



# Test

from _testfunc import testfunc

s = Solution()


testfunc(s.maxVowels, ("abciiidef", 3), 3)
testfunc(s.maxVowels, ("aeiou", 2), 2)
testfunc(s.maxVowels, ("leetcode", 3), 2)
testfunc(s.maxVowels, ("tryhard", 4), 1)