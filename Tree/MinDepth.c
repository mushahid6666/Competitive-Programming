/*Given a binary tree, find its minimum depth.

The minimum depth is the number of nodes along the shortest path from the root node down to the nearest leaf node.

 NOTE : The path has to end on a leaf node. 
Example :

         1
        /
       2
min depth = 2.*/
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
 */
 
int min(int a,int b){
    return a<b?a:b;
}
int max(int a,int b){
    return a>b?a:b;
}
int height(treenode *root){
    if(root == NULL)
        return 0;
    //If the node has single child then it should ignore the empty child value
   // & consider only the valid child height
    if(root->left==NULL && root->right!=NULL)
        return ((max(height(root->left),height(root->right))) + 1);
    else if(root->right==NULL && root->left!=NULL)
        return ((max(height(root->left),height(root->right))) + 1);
    else//if two child exist resturn the min height from the sub tree
        return ((min(height(root->left),height(root->right))) + 1);
}
int minDepth(treenode* A) {
    return height(A);
}

