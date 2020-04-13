# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def diameterOfBinaryTree(self, root: TreeNode) -> int:
        def height(node):
            if node == None:
                return 0
            return 1 + max(height(node.left) ,height(node.right))
        if root == None:
            return 0
        
        def diam(node):
            if node == None:
                return 0
            lheight = height(node.left) 
            rheight = height(node.right)
                             
            ldiam = diam(node.left)
            rdiam = diam(node.right)

                             
            return max(lheight + rheight, max(ldiam, rdiam)) 
                             
        return diam(root)