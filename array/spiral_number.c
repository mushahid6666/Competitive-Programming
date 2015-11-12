#include <stdio.h>
#include <stdlib.h>
/**
 * @input A : Integer
 *
 * @Output 2D int array. You need to malloc memory for result 2D array.
 * Fill in number_of_rows as row, number_of_columns as columns
 */
int ** prettyPrint(int A, int *number_of_rows, int *number_of_columns) {
    // SAMPLE CODE
    int i;
    if(A == 1) {
        *number_of_rows = 1;
        *number_of_columns = 1;
        int **result = (int **)malloc((*number_of_rows) * sizeof(int *));
        for(i = 0; i < *number_of_rows; i++)
            result[i] = malloc((*number_of_rows) * sizeof(int));
        result[0][0] = 1;
        return 1;
    }
    else {
        *number_of_rows = (A*2) - 1;
        *number_of_columns = (A*2) - 1;
        int **result = (int **)malloc((*number_of_rows) * sizeof(int *));
        // DO STUFF HERE
        for(i = 0; i < *number_of_rows; i++)
            result[i] = malloc((*number_of_rows) * sizeof(int));

        int T = 0;
        int L = 0;
        int B = *number_of_rows-1;
        int R = *number_of_rows-1;
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
}

int main(int argc, char *argv[]){
    int a,b;
    int ** result = prettyPrint(1,&a,&b);
    for (int i = 0; i < a; ++i) {
        for (int j = 0; j < b; ++j) {
            printf("%d ",result[i][j]);
        }
        printf("\n");
    }
}
