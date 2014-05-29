# Definition for a  binary tree node
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    # @param root, a tree node
    # @return a list of integers
    def inorderTraversal(self, root):
        left = list()
        right = list()
        if root == None:
            return list()
        if root.left != None:
            left = self.inorderTraversal(root.left)
        if root.right != None:
            right = self.inorderTraversal(root.right)

        left.append(root.val)
        left = left + right
        return left

