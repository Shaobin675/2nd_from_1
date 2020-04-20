#
# @lc app=leetcode id=2 lang=python3
#
# [2] Add Two Numbers
#
# https://leetcode.com/problems/add-two-numbers/description/
#
# algorithms
# Medium (31.02%)
# Likes:    5046
# Dislikes: 1290
# Total Accepted:    853.9K
# Total Submissions: 2.8M
# Testcase Example:  '[2,4,3]\n[5,6,4]'
#
# You are given two non-empty linked lists representing two non-negative
# integers. The digits are stored in reverse order and each of their nodes
# contain a single digit. Add the two numbers and return it as a linked list.
# 
# You may assume the two numbers do not contain any leading zero, except the
# number 0 itself.
# 
# Example:
# 
# 
# Input: (2 -> 4 -> 3) + (5 -> 6 -> 4)
# Output: 7 -> 0 -> 8
# Explanation: 342 + 465 = 807.
# 
# 
#

# @lc code=start
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def addTwoNumbers(self, l1: ListNode, l2: ListNode) -> ListNode:
        h1, h2= l1, l2
        head=ListNode(0)
        p=head
        more=0
        while h1 and h2:
            v=h1.val+h2.val+more
            
            if v>=10:
                v%=10
                more=1
            else:
                more=0
            node=ListNode(v)
            p.next=node
            p=p.next
            h1=h1.next
            h2=h2.next
        #h1 not None
        while h1:
            v=h1.val+more
            if v>=10:
                v%=10
                more=1
            else:
                more=0
            node=ListNode(v)
            p.next=node
            p=p.next
            h1=h1.next
        #h2 not None
        while h2:
            v=h2.val+more
            if v>=10:
                v%=10
                more=1
            else:
                more=0
            node=ListNode(v)
            p.next=node
            p=p.next
            h2=h2.next
        #if extra digit
        if more>0:
            node=ListNode(more)
            p.next=node
        return head.next
# @lc code=end

