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

Node* findLCAUtil(Node *root, int n1, int n2, int *v1, int *v2)
{
    // Base case
    if(root == NULL) return NULL;

    // If either n1 or n2 matches with root's key, report
    // the presence by returning root (Note that if a key is
    // ancestor of other, then the ancestor key becomes LCA
    if(root->data == n1) {
        *v1 = true;
        return root;
    }

    if( root->data == n2){
        *v2 = true;
        return root;
    }

    // Look for keys in left and right subtrees
    Node *leftLCA = findLCAUtil(root->left, n1, n2, v1, v2);
    Node *rightLCA = findLCAUtil(root->right, n1, n2, v1, v2);

    // If both of the above calls return Non-NULL, then one key
    // is present in once subtree and other is present in other,
    // So this node is the LCA
    if(leftLCA && rightLCA)
        return root;

    // Otherwise check if left subtree or right subtree is LCA
    return (leftLCA != NULL)?leftLCA:rightLCA;
}

bool find(Node* root, int data)
{
    if(root == NULL)
        return false;

    if (root->data == data || find(root->left, data) ||  find(root->right, data))
        return true;

    // Else return false
    return false;


}

Node* findLCA(Node* root , int n1, int n2)
{
    int v1 = false;
    int v2 = false;
    if(!find(root, n1))
        return -1;
    if(!find(root, n2))
        return -1;

    Node* temp = findLCAUtil(root, n1, n2, &v1, &v2);

    if((v1 && v2) || (v1 && find(temp, n1)) || (v2 && find(temp, n2)))
        return temp;

    return NULL;

}
int main()
{
    Node * root = newnode(1);
    root->left = newnode(2);
    root->right = newnode(3);
    root->left->left = newnode(4);
    root->left->right = newnode(5);
    root->right->left = newnode(6);
    root->right->right = newnode(7);

    printf("LCA(4, 10) = %d",findLCA(root, 4, 10)->data);
    printf("\nLCA(4, 6) = %d",findLCA(root, 4, 6)->data);
    printf("\nLCA(3, 4) = %d",findLCA(root, 3, 4)->data);
    printf("\nLCA(2, 4) = %d",findLCA(root, 2, 4)->data);
}