# Definition for a  binary tree node
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    # @param root, a tree node
    # @return an integer
    def maxDepth(self, root):
        depth = 0
        leftDept = 0
        rightDept = 0
        if root == None:
            return 0
        if root.left != None:
            leftDept = self.maxDepth(root.left)
        if root.right != None:
            rightDept = self.maxDepth(root.right)
        if leftDept >= rightDept:
            return leftDept +1
        else:
            return rightDept+1