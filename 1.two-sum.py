#
# @lc app=leetcode id=1 lang=python3
#
# [1] Two Sum
#
# https://leetcode.com/problems/two-sum/description/
#
# algorithms
# Easy (44.45%)
# Likes:    11737
# Dislikes: 406
# Total Accepted:    2.1M
# Total Submissions: 4.7M
# Testcase Example:  '[2,7,11,15]\n9'
#
# Given an array of integers, return indices of the two numbers such that they
# add up to a specific target.
# 
# You may assume that each input would have exactly one solution, and you may
# not use the same element twice.
# 
# Example:
# 
# 
# Given nums = [2, 7, 11, 15], target = 9,
# 
# Because nums[0] + nums[1] = 2 + 7 = 9,
# return [0, 1].
# 
# 
#
class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        pair={}
        for i, val in enumerate(nums):
            if target-val in pair:
                return [pair[target-val], i]
            else:
                pair[val]=i
        return []










        '''
        dic=collections.defaultdict(int)
        for i in range(len(nums)):
            if target-nums[i] in dic:
                return [dic[target-nums[i]], i]
            else:
                dic[nums[i]]=i
        return []
        '''
