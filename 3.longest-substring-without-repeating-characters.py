#
# @lc app=leetcode id=3 lang=python3
#
# [3] Longest Substring Without Repeating Characters
#
# https://leetcode.com/problems/longest-substring-without-repeating-characters/description/
#
# algorithms
# Medium (29.82%)
# Likes:    8416
# Dislikes: 508
# Total Accepted:    1.4M
# Total Submissions: 4.8M
# Testcase Example:  '"abcabcbb"'
#
# Given a string, find the length of the longest substring without repeating
# characters.
# 
# 
# Example 1:
# 
# 
# Input: "abcabcbb"
# Output: 3 
# Explanation: The answer is "abc", with the length of 3. 
# 
# 
# 
# Example 2:
# 
# 
# Input: "bbbbb"
# Output: 1
# Explanation: The answer is "b", with the length of 1.
# 
# 
# 
# Example 3:
# 
# 
# Input: "pwwkew"
# Output: 3
# Explanation: The answer is "wke", with the length of 3. 
# ⁠            Note that the answer must be a substring, "pwke" is a
# subsequence and not a substring.
# 
# 
# 
# 
# 
#

# @lc code=start
class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        #4:55-5:05, 10min
        p1, p2=0, 0
        
        l=len(s)
        result=1
        if l==0:
            return 0
        tmp_dic={}
        while l>p2 and l>p1:
            
            #print(tmp_dic)
            if p2<l and s[p2] not in tmp_dic:
                tmp_dic[s[p2]]=p2
                result=max(p2-p1+1, result)
                p2+=1
            else:
                del tmp_dic[s[p1]]
                p1+=1
            #p2=p1+1
                
        return result
            
# @lc code=end

