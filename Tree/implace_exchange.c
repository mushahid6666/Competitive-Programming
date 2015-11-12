
  // Definition for binary tree
#include<stdio.h>
#include<stdlib.h>
  struct TreeNode {
     int val;
      struct TreeNode *left;
      struct TreeNode *right;
 };
  
  typedef struct TreeNode treenode;
  
 treenode* treenode_new(int val) {
      treenode* node = (treenode *) malloc(sizeof(treenode));
      node->val = val;
      node->left = NULL;
      node->right = NULL;
      return node;
  }
/**
 * @input root : Root pointer of the tree 
 * 
 * @Output root pointer of tree.
 */
 void pre(treenode* root){
 	if(root->left==NULL && root->right==NULL)
 		return;
 	if(root->left==NULL && root->right==NULL){
		treenode* temp=NULL;
		temp = root->left;
		root->left = root->right;
		root->right = temp;
		printf("swapping %d and %d\n", root->left->val,root->right->val);
	}
	if(root->left!=NULL)
 		pre(root->left);
 	if(root->right!=NULL)
 		pre(root->right);
 }
treenode* invertTree(treenode* root) {
	pre(root);
	return root;
}
void preorder(treenode* root){
	if(root==NULL)
		return;
	printf("%d, \n", root->val);
	preorder(root->left);
	preorder(root->right);
}
int main(int argc, char const *argv[])
{
	/* code */
	treenode* root = treenode_new(1);
	root->left = treenode_new(2);
	invertTree(root);
	preorder(root);
	return 0;
}