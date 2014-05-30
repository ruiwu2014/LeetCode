# Definition for a  binary tree node
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None
Not Done
class Solution:
    # @param root, a tree node
    # @return a boolean
    def isBalanced(self, root):
        res = self.isBalancedR(root)
        return True if res else False


    def isBalancedR(self,root):
        if root is None:
            return 0
        if root.left is None:
            llen = 0
        else:
            llen = self.isBalanced(root.left)

        if root.right is None:
            rlen = 0
        else:
            rlen = self.isBalanced(root.right)
        if llen < 0 or rlen < 0: #some node is unbalanced
            return -1
        elif abs(llen-rlen)>1:
            return -1
        else:
            return max(llen,rlen)+1


