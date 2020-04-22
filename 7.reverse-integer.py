#
# @lc app=leetcode id=7 lang=python3
#
# [7] Reverse Integer
#
# https://leetcode.com/problems/reverse-integer/description/
#
# algorithms
# Easy (25.65%)
# Likes:    3078
# Dislikes: 4850
# Total Accepted:    1M
# Total Submissions: 4M
# Testcase Example:  '123'
#
# Given a 32-bit signed integer, reverse digits of an integer.
# 
# Example 1:
# 
# 
# Input: 123
# Output: 321
# 
# 
# Example 2:
# 
# 
# Input: -123
# Output: -321
# 
# 
# Example 3:
# 
# 
# Input: 120
# Output: 21
# 
# 
# Note:
# Assume we are dealing with an environment which could only store integers
# within the 32-bit signed integer range: [−2^31,  2^31 − 1]. For the purpose
# of this problem, assume that your function returns 0 when the reversed
# integer overflows.
# 
#

# @lc code=start
class Solution:
    def reverse(self, x: int) -> int:
        
        neg=""
        if x<0:
            neg='-' 
            x=0-x
        
        s=str(x)
        s=s[::-1]
        ans=int(s)
        if neg=='-':
            ans=0-ans
        if ans>2**31-1 or ans<-2**31:
            return 0
        return ans        
# @lc code=end

