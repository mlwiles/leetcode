# https://leetcode.com/problems/longest-palindromic-substring/

# Given a string s, return the longest palindromic substring in s.

# Example 1:
# Input: s = "babad"
# Output: "bab"
# Explanation: "aba" is also a valid answer.

# Example 2:
# Input: s = "cbbd"
# Output: "bb"
 
# Constraints:
# 1 <= s.length <= 1000
# s consist of only digits and English letters.

class Solution:
    def longestPalindrome(self, s: str):
        index = 0
        longest = 0
        templongest = 0
        starter = 0
        tempstr = ""
        while starter < len(s):
            while index < len(s):
                letter = s[index]
                if tempstr and tempstr.find(letter) > -1:
                    if templongest > longest:
                        longest = templongest
                    templongest = 0
                    tempstr = letter
                else:
                    tempstr =  tempstr + letter
                    templongest = len(tempstr)
                index += 1   
                if templongest > longest:
                        longest = templongest
            starter += 1
            index = starter
            tempstr = ""
        return longest


sol = Solution()
print(sol.longestPalindrome("babad"))
print(sol.longestPalindrome("cbbd"))