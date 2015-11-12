#include<stdio.h>
#include<stdlib.h>
#include<string.h>
int string_length(char *pointer);
void reverse(char *string);
char* findDigitsInBinary(int A);
void reverse(char *string) 
{
   int length, c;
   char *begin, *end, temp;
 
   length = string_length(string);
   begin  = string;
   end    = string;
 
   for (c = 0; c < length - 1; c++)
      end++;
 
   for (c = 0; c < length/2; c++)
   {        
      temp   = *end;
      *end   = *begin;
      *begin = temp;
 
      begin++;
      end--;
   }
}
 
int string_length(char *pointer)
{
   int c = 0;
 
   while( *(pointer + c) != '\0' )
      c++;
 
   return c;
}

char* findDigitsInBinary(int A) {
	// SAMPLE CODE
	 //printf("%d",A);	
	  char* result = (char *)malloc(100 * sizeof(char));
	  if(A == 1) {
	      result[0] = 1;
	      //printf("%s",result);
	      return 1;
	  }
		printf("coming here\n");
	  int rem;
	  int i =0;
	  while(A > 0) {
	      rem = A%2;
	      result[i] = rem;
	      A= A/2;
	      i++;
	  }
	  reverse(result);
	  
	  return result; 
	 
}
int main(int argc, char* argv[])
{
	char *result = findDigitsInBinary(atoi(argv[1]));	
	printf("%s\n",result);
}
