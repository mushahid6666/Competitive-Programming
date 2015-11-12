/**
 * @input A : Integer
 * 
 * @Output 2D int array. You need to malloc memory for result 2D array. 
 * Fill in number_of_rows as row, number_of_columns as columns 
 */
#include <stdlib.h>
#include <stdio.h>
int ** prettyPrint(int A, int *number_of_rows, int *number_of_columns) {
    // SAMPLE CODE

    *number_of_rows = A;
    *number_of_columns = A;
    int **result = (int **)malloc(A * sizeof(int *));
    // DO STUFF HERE
    int i;
    for(i = 0; i < A; i++)
        result[i] = malloc(A * sizeof(int));

    int T = 0;
    int L = 0;
    int B = A-1;
    int R = A-1;
    int dir = 0;
    int count = A;
    int j,k,p;
    while(T <=B && L <=R) {
        if (dir == 0){
            for ( i = L; i <= R; ++i) {
                result[T][i]  = count;
            }
            T++;
        }
        if(dir ==1) {
            for ( j = T; j <= B; ++j) {
                result[j][R] = count;
            }
            R--;
        }
        if(dir ==2) {
            for (k = R; k >= L; k--) {
                result[B][k] = count;
            }
            B--;
        }
        if(dir ==3) {
            for (p = B; p >= T; p--) {
                result[p][L] = count;
            }
            L++;
        }
        dir = (dir+1)%4;
        if(dir == 0)
            count --;
    }
    return result;
}

int main(int argc, char *argv[]) {
    int A = atoi(argv[1]);
    int ** result;
    int row;
    int col;
    result = prettyPrint(A,&row,&col);
    for (int i = 0; i < row; ++i) {
        for (int j = 0; j <col; ++j) {
            printf("%d ",result[i][j]);
        }
        printf("\n");
    }
}
