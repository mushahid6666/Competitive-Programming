#include<stdio.h>
#include<stdlib.h>
int square(int num) 
{ 
	int i,result=0; 
	for(i=0;i<num;i++) 
	{ 
		result=result+num; 
	} 
	return result; 
}
int main(int argc, char *argv[])
{
	if(argv[1]){
		int result = square(atoi(argv[1]));
		printf("result = %d\n",result);
	}
	else
		printf("Pass number to calculate square in argv[1]\n");
}
