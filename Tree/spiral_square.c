/**
 * @input A : Integer
 * 
 * @Output 2D int array. You need to malloc memory. Fill in number_of_rows as row, number_of_columns as columns 
 */
#include<stdio.h>
#include<stdlib.h>
int ** generateMatrix(int A, int *number_of_rows, int *number_of_columns) {
	// SAMPLE CODE
          int i,j,k,p;
          *number_of_rows = A;
          *number_of_columns = A;
          int **result = (int **)malloc(A * sizeof(int *));
          int L = 0;
          int R = *number_of_columns - 1;
          int B = *number_of_rows - 1;
          int T = 0;
          int dir = 0;
          int counter = 1;
          while(T < B)
          {
              if(dir == 0) {
                  for(  i =L; i <= R; ++i){
                      result [T][i] = counter;
                      counter++;
                  }
                  T++;
                  dir++;
              }
              else if(dir == 1) {
                  for( j =T; j <= B; ++j){
                      result [j][R] = counter;
                      counter++;
                  }
                  R--;
                  dir++;
              }
              else if(dir == 2) {
                  for( k =R; k <= L; --k){
                      result [B][k] = counter;
                      counter++;
                  }
                  B--;
                  dir++;
              }
              else if(dir == 3) {
                  for( p =B; p <= T; --p){
                      result [p][L] = counter;
                      counter++;
                  }
                  L++;
                  dir++;
              }
              
              if((dir %4) == 0) {
                  dir =0;
              }
              
              
          }
          
          
         return result;
         
         
}

int main()
{
  int A = 3;
 int *c,*d;
int **result = (int **)malloc(A * sizeof(int *));
  generateMatrix(A, c,d);
 int i,j;
  for(i = 0; i< A; i++) {
    for(j=0 ; j<A; j++) {
       printf("%d ", result[i][j]);
  }
}
}

