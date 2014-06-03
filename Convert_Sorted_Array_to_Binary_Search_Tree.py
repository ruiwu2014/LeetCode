# Definition for a  binary tree node
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    # @param num, a list of integers
    # @return a tree node
    def sortedArrayToBST(self, num):
        if not num:
            return None
        return self.sortedArrayToBSTR(0, len(num)-1)
        
    def sortedArrayToBSTR(self,num,start,end):
        if start == end:
            node = TreeNode(num[start])
            return node
        if start < end:
            mid = (start+end)/2
            node = TreeNode(num[mid])
            if mid == start:
                node.left = None
                node.right = TreeNode(num[end])
                return node
            node.left = self.sortedArrayToBSTR(num, start, mid-1)
            node.right = self.sortedArrayToBSTR(num, mid+1, end)   
        return node 