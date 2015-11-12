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

void Deletelist(NODE **head)
{
    NODE *current,*next;
    current = (*head);

    while(current != NULL){
        printf("deleting node %d\n",current->data);
        next = current->link;
        free(current);
        current = next;
    }
    (*head) = NULL;
}
int main()
{
    NODE *head = NULL;
    int n;
    //input
    printf("enter the number of items in the linked list data\n");
    scanf("%d",&n);
    push(&head,n);
    printf("Delting the list\n");
    Deletelist(&head);
}
