# Definition for a  binary tree node
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    # @param root, a tree node
    # @return a list of integers
    def preorderTraversal(self, root):
        left = list()
        right = list()
        if root == None:
            return list()
        mid  = [root.val]
        if root.left != None:
            left = self.preorderTraversal(root.left)
        if root.right != None:
            right =self.preorderTraversal(root.right)

        mid = mid + left
        mid = mid + right
        return mid