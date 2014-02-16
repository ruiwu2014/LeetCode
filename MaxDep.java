/*
Given a binary tree, find its maximum depth.

The maximum depth is the number of nodes along the longest path from the root node down to the farthest leaf node.
*/


/**
 * Definition for binary tree
 * public class TreeNode {
 *     int val;
 *     TreeNode left;
 *     TreeNode right;
 *     TreeNode(int x) { val = x; }
 * }
 */
public class Solution {
    public int maxDepth(TreeNode root) {
        if(root == null)
            return 0;
        
        int left = root.left==null?0:maxDepth(root.left);
        int right = root.right == null?0:maxDepth(root.right);
        return 1+(left>=right?left:right);
    }
    
     
}
