#include<stdio.h>
#include<stdlib.h>

/* Change a tree so that the roles of the left and
	right pointers are swapped at every node.

So the tree...
	4
	/ \
	2 5
	/ \
1 3

is changed to...
	4
	/ \
	5 2
		/ \
	3 1
*/
struct node 
{
	int data;
	struct node* left;
	struct node* right;
};
struct node* newNode(int data)

{
	struct node* node = (struct node*)
						malloc(sizeof(struct node));
	node->data = data;
	node->left = NULL;
	node->right = NULL;

	return(node);
}

struct node* mirror(struct node* node)
{
	if (node==NULL)
		return NULL;
	else
	{

		/* swap the pointers in this node */
		struct node *newnode	 = newNode(node->data);
		newnode->left = mirror(node->right);
		newnode->right = mirror(node->left);
		return newnode;
	}
}
/* if inplace
struct node* mirror(struct node* node)
{
	if (node==NULL)
		return ;
	else
	{
		mirror(node->left);
		mirror(node->right);
		struct node *swap;
		swap = node->left;
		node->left = node->right;
		node->right = swap;
	}
}*/
