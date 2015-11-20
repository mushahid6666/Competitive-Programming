/*You are given a pointer to the root of a binary tree. Print the top view of the binary tree. 
You only have to complete the function. 
For example :

     3
   /   \
  5     2
 / \   / \
1   4 6   7
 \       /
  9     8
Top View : 1 -> 5 -> 3 -> 2 -> 7*/
/*
struct node
{
    int data;
    node* left;
    node* right;
};

*/
static int ht = 0;
int max(int a,int b){
    return a>b?a:b;
}
int height(node *root){
    if(root == NULL)
        return 1;
    return ((max(height(root->left),height(root->right))) + 1);
}
//Direction 0->left, 1->right
void print_node(node *root,int ht, int direction,int counter){
    if(direction == 0){
        //print all the left nodes starting from the last left node
        if(root == NULL) return;
        print_node(root->left,ht-1,0,counter);
        printf("%d ",root->data);
    }
    else {
        //print all the right nodes while going down the tree
        if(root == NULL) return;
        if(counter != ht) {
            printf("%d ",root->data);
        }
        print_node(root->right,ht, 1,counter -1);
        
    }
} 
void top_view(node * root)
{
    ht = height(root);
    int counter = 0;
    print_node(root,ht,0,counter);
    counter  = ht;
    print_node(root,ht,1,ht);
  
}

