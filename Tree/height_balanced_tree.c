//
#include <stdio.h>
#include <stdlib.h>
// Definition for binary tree
struct TreeNode {
    int val;
    struct TreeNode *left;
    struct TreeNode *right;
};

typedef struct TreeNode treenode;

treenode *treenode_new(int val) {
    treenode *node = (treenode *) malloc(sizeof(treenode));
    node->val = val;
    node->left = NULL;
    node->right = NULL;
    return node;
}
treenode *sortedArrayToBSTGenerate(int * A, int start, int end){
    if(start>end)
        return NULL;
    int mid = (start+end)/2;
    treenode *newnode = treenode_new(A[mid]);
    newnode->left = sortedArrayToBSTGenerate(A,start,mid-1);
    newnode->right = sortedArrayToBSTGenerate(A,mid+1,end);
    return newnode;
}
treenode *sortedArrayToBST(int *A,int len){
        if(len==0)
            return NULL;
        return sortedArrayToBSTGenerate(A,0,len-1);
}

void inorder(treenode *A){
    if(A==NULL)
        return;
    inorder(A->left);
    printf("%d, ",A->val);
    inorder(A->right);
}

int main(int argc,char* argv[]){
    int A[3] = {1,4,8};
    treenode* root = sortedArrayToBST(A,3);
    inorder(root);

}

