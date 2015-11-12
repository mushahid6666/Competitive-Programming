//
// Created by Mushahid Alam on 10/6/15.
//
#include <stdlib.h>
#include <stdio.h>
#include <math.h>
int isPower(int A) {
    if(A == 1)
        return 1;
    if(A == 2)
        return 0;
    if(A == 4)
        return 1;
    int counter;
    int result;
    for (int i = 2; i < A/2; ++i) {
        counter = i;
        result = counter*counter;
        while (result <= A) {
            if (result == A)
                return 1;
            result = result * counter;
        }
    }
    return 0;
}
int main(int argc, char*argv[]){
    int number = atoi(argv[1]);
    printf("%d",isPower(number));
}