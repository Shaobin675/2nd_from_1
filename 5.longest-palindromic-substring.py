#
# @lc app=leetcode id=5 lang=python3
#
# [5] Longest Palindromic Substring
#
# https://leetcode.com/problems/longest-palindromic-substring/description/
#
# algorithms
# Medium (27.79%)
# Likes:    4247
# Dislikes: 394
# Total Accepted:    643.8K
# Total Submissions: 2.3M
# Testcase Example:  '"babad"'
#
# Given a string s, find the longest palindromic substring in s. You may assume
# that the maximum length of s is 1000.
# 
# Example 1:
# 
# 
# Input: "babad"
# Output: "bab"
# Note: "aba" is also a valid answer.
# 
# 
# Example 2:
# 
# 
# Input: "cbbd"
# Output: "bb"
# 
# 
#

# @lc code=start
class Solution:
    def longestPalindrome(self, s: str) -> str:
        l=len(s)
        self.ans=""
        for i in range(len(s)):
            self.helper(i, i, s)
            self.helper(i, i+1, s)
        return self.ans
        
        
    def helper(self, left, right, s):
        while left>=0 and right <len(s) and s[left]==s[right]:
            left-=1
            right+=1
        tmp=s[left+1:right]
        if len(tmp)>len(self.ans):
            self.ans=tmp        
# @lc code=end

