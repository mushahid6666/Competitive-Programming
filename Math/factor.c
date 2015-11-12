#include<stdio.h>
#include<stdlib.h>
#include<math.h>
//#include<alloc.h>
/**
 * @input A : Integer
 * 
 * @Output Integer array. You need to malloc memory for result array, and fill result's length in length_of_array
 */
 int cmpfunc (const void * a, const void * b)
{
   return ( *(int*)a - *(int*)b );
}

int* allFactors(int A, int *length_of_array) {
	// SAMPLE CODE
        
         //*length_of_array = 1000; // length of result array
          int *result = (int *) malloc(1000 * sizeof(int));
          // DO STUFF HERE. NOTE: length_of_array is inaccurate in this example. 
          int i;
          //int counter;
            *length_of_array = 0;
          if(A == 1) {
              result[(*length_of_array)] = 1;
              *length_of_array = *length_of_array+ 1;
              return result;
          }
          

          int limit = sqrt(A);
	  printf("%d = limit ",limit);
          int second ;
          for(i =1 ; i <= limit; i++){
	      //printf("%d",i);
              if((A%i) == 0) {
		//printf("%d\n", i);
                result[(*length_of_array)] = i ;
                *length_of_array = *length_of_array+ 1;
                //if(i != limit )   {
                    second = A/i;
                    if(second != A) {
                    result[(*length_of_array)] = second;
                    *length_of_array = *length_of_array+ 1;
                    }
                //}
              }
          }
          result[(*length_of_array)] = A;
          *length_of_array = *length_of_array+ 1;
          qsort(result, *length_of_array, sizeof(int), cmpfunc);
          
          return result;
         
}
int main(int argc, char *argv[])
{
	int i;
	int A = 38808;
	int *length_of_array = (int*)malloc(sizeof(int));
	int *result= allFactors(A,length_of_array);
	//printf("%d",*length_of_array);
	for(i=0;i<*length_of_array; i++){
		printf("%d \n",result[i]);
	}
}
