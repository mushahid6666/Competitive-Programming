//
// Created by Mushahid Alam on 10/8/15.
//
#include <stdio.h>
#include <stdlib.h>
#include <math.h>
struct ListNode {
    int val;
    struct ListNode *next;
};

typedef struct ListNode listnode;
listnode* head;

listnode* listnode_new(int val) {
    listnode* node = (listnode *) malloc(sizeof(listnode));
    node->val = val;
    node->next = NULL;
    return node;
}

/*@input A : Head pointer of linked list

@Output head pointer of list.
/*/

int lenght(listnode* A) {
    int counter = 0;
    if(A == NULL)
        return 0;
    if(A->next == NULL)
        return 1;
    listnode* temp = A;
    while (temp != NULL){
        temp = temp->next;
        counter++;
    }
    return counter;
}
listnode* add(listnode* A, int *counter) {
    if (A == NULL)
        return NULL;
    listnode *temp = add(A->next, counter);

    if(*counter == 0)
        return NULL;
    if (temp == NULL) {
        head->val = A->val - head->val;
        (*counter)--;
        return head->next;
    }
    else {
        temp->val = A->val - temp->val;
        (*counter)--;
        return temp->next;
    }
}

listnode* subtract(listnode* A) {
    head = A;
    int len = lenght(A);
    int counter ;
    if(len%2 != 0)
     counter = floor(len/2);
    else
        counter = len/2;
    add(A,&counter);
    return head;
}
int main(int argc, char* argv[]){
    printf("%f",floor(3/2));
    listnode* A = listnode_new(88);
    A->next = listnode_new(15);
    A->next->next = listnode_new(98);
    A = subtract(A);
    listnode*  temp = A;
    for (int i = 0; i < 3; ++i) {
        printf("%d ",temp->val);
        temp= temp->next;
    }

}

