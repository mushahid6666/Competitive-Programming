//
// Created by Mushahid Alam on 9/12/15.
//
#include <stdio.h>
#include <stdlib.h>

int main()
{
    int m,n;
    printf("enter the size of the array in m*n\n");
    scanf("%d%d",&m,&n);
    int *A[m];
    for (int k = 0; k <m ; ++k) {
        A[k] = (int*)malloc(n*sizeof(int));
    }
    printf("enter the elements in row wize\n");
    for (int i = 0; i <m ; ++i) {
        for (int j = 0; j < n; ++j) {
            scanf("%d",&A[i][j]);
        }
    }
    int T = 0;
    int L = 0;
    int B = m-1;
    int R = n-1;
    int dir = 0;
    while(T <=B && L <=R) {
        if (dir == 0){
            for (int i = L; i <= R; ++i) {
                printf("%d ", A[T][i]);
            }
            T++;
        }
        if(dir ==1) {
            for (int i = T; i <= B; ++i) {
                printf("%d ", A[i][R]);
            }
            R--;
        }
        if(dir ==2) {
            for (int i = R; i >= L; i--) {
                printf("%d ", A[B][i]);
            }
            B--;
        }
        if(dir ==3) {
            for (int i = B; i >= T; i--) {
                printf("%d ", A[i][L]);
            }
            L++;
        }
        dir = (dir+1)%4;
    }
}

