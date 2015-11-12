/**
 * @input A : Integer
 * 
 * @Output Integer array. You need to malloc memory for result array, and fill result's length in length_of_array
 */
#include<stdio.h>
#include<stdlib.h>
#include<string.h>
int* sieve(int A, int *length_of_array) {
	// SAMPLE CODE
        
          *length_of_array = 0;
          //result = 1000;// length of result array
          int *result = (int *) malloc(1000 * sizeof(int));
          int *sieve = (int *) malloc(1000 * sizeof(int));
          // DO STUFF HERE. NOTE : length_of_array is inaccurate here. 
          int i;
          for(i=0;i<=A;i++)
            sieve[i]=1;
          sieve[0]=0;
          sieve[1]=0;
          int j,k;
          for(j=2;j<=A;j++)
          {
              if(sieve[j]==1){
                  for(k=2;j*k<=A;k++){
             		sieve[i*j]=0;
			printf("%d scratching ",i*j);
                  }
              }
          }
          j=0;
          for(i =0 ;i <=A;i++){
              if(sieve[i]==1){
                result[j++] = i;
                *length_of_array = *length_of_array +1;
              }
          }
          
          return result;
         
}
int main(int argc,char *argv[])
{
	int A =10;
	int *length_of_array = (int*)malloc(sizeof(int));
	int *result = sieve(A,length_of_array);
	int i;
	for(i=0;i<*length_of_array;i++)
		printf("%d ",result[i]);
	
}

