/**
 * Definition for binary tree
 * struct TreeNode {
 *     int val;
 *     TreeNode *left;
 *     TreeNode *right;
 *     TreeNode(int x) : val(x), left(NULL), right(NULL) {}
 * };
 */
class Solution {
public:
    int maxDepth(TreeNode *root) {

        int leftH = 0, rightH = 0;
        if(root == NULL){
            return 0;
        }

        if(root->left != NULL){
            leftH += maxDepth(root->left);
        }
        if(root->right != NULL){
            rightH += maxDepth(root->right);
        }
        return 1+(leftH>=rightH?leftH:rightH);
    }
};