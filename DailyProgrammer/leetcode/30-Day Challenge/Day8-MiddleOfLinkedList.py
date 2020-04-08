# -*- coding: utf-8 -*-
"""
Created on Wed Apr  8 14:05:21 2020

@author: Zach
"""


# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def middleNode(self, head: ListNode) -> ListNode:
        length = 0
        node = head
        while node != None:
            
            node = node.next
            length += 1
        i = int(length/2)       
        for j in range(i):
            head = head.next
            
        return head