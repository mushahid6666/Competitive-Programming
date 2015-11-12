//
// Created by Mushahid Alam on 10/5/15.
//
#include <stdio.h>
#include <stdlib.h>



struct node
{
    int data;
    struct node* left;
    struct node* right;
};


int max(int a, int b){
    return a>b?a:b;
}
int height(struct node* root)
{
    if(root == NULL)
        return 0;
    else
        return (max(height(root->left),height(root->right))+1);
}



void PrintGivenLevel(int level,struct node* root)
{
    if(root == NULL)
        return;
    if(level == 0)
        printf("%d ",root->data);
    return;
    PrintGivenLevel(level-1,root->left);
    PrintGivenLevel(level-1,root->right);

}

void LevelOrder(struct node* root)
{
    int i=0;
    int ht =0;
    ht= height(root);
    for(i=0;i<ht;i++)
        PrintGivenLevel(i,root);
}
struct node* insert(int data){
    struct node* root = (struct node *)malloc (sizeof(struct node));
    root->data = data;
    return root;
}
int main(){
    struct node* root = (struct node *)malloc (sizeof(struct node));
    root->data = 3;
    root->left = insert(5);
    root->right = insert(2);
    root->left->left = insert(1);
    root->left->right = insert(4);
    root->right->left = insert(5);
    LevelOrder(root);


}