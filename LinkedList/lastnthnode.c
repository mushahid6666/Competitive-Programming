//
// Created by Mushahid Alam on 9/10/15.
//
#include <stdio.h>
#include <stdlib.h>
typedef struct node
{
    int data;
    struct node *link;
}NODE;

void push(NODE **head, int n)
{
    int ndata;
    NODE *last = (*head);

    printf("enter the nodes data\n");
    for (int i = 0; i <n; ++i) {
        scanf("%d",&ndata);
        NODE *newnode = (NODE*)malloc(sizeof(NODE));
        newnode->data = ndata;
        newnode->link = NULL;
        if(last == NULL){
            last = newnode;
            (*head) = last;
        }
        else {
            while(last->link != NULL){
                last = last->link;
            }
            (last)->link = newnode;
        }
    }
}

void getLastNode(NODE **head, int last)
{
    int length = 0;
    NODE *temp = (*head);
    while(temp != NULL){
        temp = temp->link;
        length++;
    }
    if(length < last) {
        printf("length is lesser than the last node value entered %d length, %d last\n",length,last);
        return;
    }
    NODE *find = *head;
    for (int i = 0; i < (length-last); ++i) {
        find = find->link;
    }
    printf("Node data = %d\n",find->data);
}
int main()
{
    NODE *head = NULL;
    int last,n;
    //input
    printf("enter the number of items in the linked list data\n");
    scanf("%d",&n);
    push(&head,n);
    printf("Enter the nth node from last of which data is needed\n");
    scanf("%d",&last);
    getLastNode(&head, last);
}
