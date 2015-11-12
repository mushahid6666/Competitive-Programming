//
// Created by Mushahid Alam on 9/14/15.
//
#include <stdio.h>
#include <stdlib.h>
#include <string.h>

void test(char *s1, char *s2)
{
    int len1 = strlen(s1);
    int len2 = strlen(s2);
    int j = 0;
    int i = 0;
    for( i = 0; i < len1 && j<len2;) {
        if(s1[i] == s2[j] || s1[i] == '?'){
            j++;
            i++;
            continue;
        }
        else if(s1[i] == '*'){
            //printf("going inside * for s1[i] = %c, s2[j] = %c\n",s1[i],s2[j]);
            i++;
            if( i < len1) {
               // printf("going inside i< len1 j=%d s2[j] = %c\n",j,s2[j]);
                j++;
                while(j<len2 && s1[i] != s2[j]) {
                    //printf("incrementing j=%d\n",j);
                    j++;
                }
            }
            else {
                printf("Strings match %s & %s\n", s1, s2);
                return;
            }
        }
        else {
            printf("Strings do not match %s & %s i = %d, len1 = %d j =%d\n", s1, s2, i , len1,j);
            return;
        }
    }
    if( i < len1)
        printf("Strings do not match %s & %s i = %d, len1 = %d\n", s1, s2, i , len1);
    else
        printf("Strings match %s & %s\n", s1, s2);

}

int main()
{
    test("g*ks", "geeks"); // Yes
    test("ge?ks*", "geeksforgeeks"); // Yes
    test("g*k", "gee");  // No because 'k' is not in second
    test("*pqrs", "pqrst"); // No because 't' is not in first
    test("abc*bcd", "abcdhghgbcd"); // Yes
    test("abc*c?d", "abcd"); // No because second must have 2 instances of 'c'
    test("*c*d", "abcd"); // Yes
    test("*?c*d", "abcd"); // Yes
    return 0;
}
