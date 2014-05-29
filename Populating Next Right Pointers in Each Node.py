# Definition for a  binary tree node
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None
#         self.next = None

class Solution:
    # @param root, a tree node
    # @return nothing
    def connect(self, root):
        if root != None:
            current = [root]
            parent = 0
            child = 1
            while current:
                parent = child
                child = 0
                for i in range(0,parent-1):
                    current[i].next = current[i+1]
                current[parent-1].next = None

                while parent>0:
                    node = current[0]
                    parent -= 1
                    del current[0]
                    if node.left:
                        current.append(node.left)
                        child += 1
                    if node.right:
                        current.append(node.right)
                        child += 1




