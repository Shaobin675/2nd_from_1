#
# @lc app=leetcode id=9 lang=python3
#
# [9] Palindrome Number
#
# https://leetcode.com/problems/palindrome-number/description/
#
# algorithms
# Easy (42.96%)
# Likes:    1365
# Dislikes: 1277
# Total Accepted:    563.1K
# Total Submissions: 1.3M
# Testcase Example:  '121'
#
# Determine whether an integer is a palindrome. An integer is a palindrome when
# it reads the same backward as forward.
# 
# Example 1:
# 
# 
# Input: 121
# Output: true
# 
# 
# Example 2:
# 
# 
# Input: -121
# Output: false
# Explanation: From left to right, it reads -121. From right to left, it
# becomes 121-. Therefore it is not a palindrome.
# 
# 
# Example 3:
# 
# 
# Input: 10
# Output: false
# Explanation: Reads 01 from right to left. Therefore it is not a palindrome.
# 
# 
# Follow up:
# 
# Coud you solve it without converting the integer to a string?
# 
#

# @lc code=start
class Solution:
    def isPalindrome(self, x: int) -> bool:
        '''
        s=str(x)
        if s==s[::-1]:
            return True
        else:
            return False        
        '''
        if x<0:
            return False
        res=0
        tmp=x
        while tmp>0:
            res=res*10+tmp%10
            tmp//=10
        return x==res      
# @lc code=end

