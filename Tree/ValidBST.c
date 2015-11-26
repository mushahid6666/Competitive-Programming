/*Given a binary tree, determine if it is a valid binary search tree (BST).

Assume a BST is defined as follows:

The left subtree of a node contains only nodes with keys less than the node’s key.
The right subtree of a node contains only nodes with keys greater than the node’s key.
Both the left and right subtrees must also be binary search trees.
Example :

Input : 
   1
  /  \
 2    3

Output : 0 or False


Input : 
  2
 / \
1   3

Output : 1 or True */


/**
 * Definition for binary tree
 * struct TreeNode {
 *     int val;
 *     struct TreeNode *left;
 *     struct TreeNode *right;
 * };
 * 
 * typedef struct TreeNode treenode;
 * 
 * treenode* treenode_new(int val) {
 *     treenode* node = (treenode *) malloc(sizeof(treenode));
 *     node->val = val;
 *     node->left = NULL;
 *     node->right = NULL;
 *     return node;
 * }
 */
/**
 * @input A : Root pointer of the tree 
 * 
 * @Output Integer
 * 
 */
//  #define INT1_MAX  4294967296
//  #define INT1_MIN -4294967296
 int isBST(treenode* root,int minvalue, int maxvalue){
     if(root==NULL) return 1;
     if(root->val > minvalue && root->val < maxvalue
        && isBST(root->left,minvalue,root->val)
        && isBST(root->right,root->val,maxvalue))
        return 1;
    else{
        return 0;
    }
 }
int isValidBST(treenode* A) {
    int result = isBST(A,INT_MIN,INT_MAX);
    return result;
}

