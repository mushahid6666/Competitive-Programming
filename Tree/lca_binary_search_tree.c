//
// Created by Mushahid Alam on 9/14/15.
//

#include <stdlib.h>
#include <stdio.h>
#include <stdbool.h>
struct node
{
    int data;
    struct node* left;
    struct node* right;
};
typedef struct node Node;

Node* newnode(int data)
{
    Node* newn = (Node*)malloc(sizeof(Node));
    newn->data = data;
    newn->left = NULL;
    newn->right = NULL;
    return newn;
}

Node* findLCA(Node *root, int n1, int n2)
{
    if(root==NULL) return NULL;
    if(root->data > n1 && root->data > n2)
        return findLCA(root->left,n1,n2);
    if(root->data < n1 && root->data < n2)
        return findLCA(root->right,n1,n2);
    return root;

}

int main()
{
    Node * root = newnode(10);
    root->left = newnode(3);
    root->right = newnode(25);
    root->left->left = newnode(1);
    root->left->right = newnode(4);
    root->right->left = newnode(20);
    root->right->right = newnode(30);

    printf("LCA(1, 4) = %d",findLCA(root, 1, 4)->data);
    printf("\nLCA(4 ,20) = %d",findLCA(root, 4, 20)->data);
    printf("\nLCA(4,30) = %d",findLCA(root, 4, 30)->data);
    printf("\nLCA(3,30) = %d",findLCA(root, 3, 30)->data);
}