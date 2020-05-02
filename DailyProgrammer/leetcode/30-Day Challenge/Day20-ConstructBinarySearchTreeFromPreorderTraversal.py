# -*- coding: utf-8 -*-
"""
Return the root node of a binary search tree that matches the given preorder traversal.

(Recall that a binary search tree is a binary tree where for every node, any 
descendant of node.left has a value < node.val, and any descendant of node.right 
has a value > node.val.  Also recall that a preorder traversal displays the value
 of the node first, then traverses node.left, then traverses node.right.)
"""

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def bstFromPreorder(self, preorder: List[int]) -> TreeNode:
        
        def inserter(arr, previousNode = float("inf")):

            if arr and  arr[0] < previousNode:     
                
                current = arr.pop(0)
                currNode = TreeNode(current)
                currNode.left = inserter(arr, current)
                currNode.right = inserter(arr, previousNode)
                return currNode
            
            return None
        
        return  inserter(preorder)
