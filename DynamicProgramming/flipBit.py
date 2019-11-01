'''
Given a binary string of size N and a positive integer K, calculate the number of operations required to convert this string to
zero string by applying the following operation any number of times.
Operation: Let X is the index of first 1 bit from left side, then Flip all the Xth, X+K, X+2K, X+3K bits of string.
1 <= N <= 10^6
1 <= K <= N

Sample:
Input: 100010010011110, K = 2
Step-1:001000111001011
Step-2:000010010011110
Step-3: 000000111001011
Step-4: 000000010011110
Step-5: 000000000110100
Step-6: 000000000011110
Step-7: 000000000001011
Step-8: 000000000000001
Step-9: 000000000000000

Output=9
Brute force is easy; O(n2 / k )

Optimization thought
I believe we need to use % operator here since Xth, X+K, X+2K, X+3K that means x + pK where p= 1,2,3
that left x as reminder.

Any thought how to solve this?

As per interviwer we can solve it in O(n) time and O(1) space
'''
class Solution:

    def flipOpCount(self, string, K):
        '''
        @param A : String
        @:param K: Int
        @return an integer
        '''
        number_arr = [0] * len(string)
        for i in range(len(string)):
            if string[i] == '1':
                number_arr[i] = 1
        opCount = 0
        for i in range(len(number_arr)):
            if number_arr[i] == 1:
                number_arr[i]=0
                for j in range(i+K, len(number_arr), K):
                    if number_arr[j] == 1:
                        number_arr[j] = 0
                    else:
                        number_arr[j] = 1
                opCount+=1
            if i==len(number_arr)-1:
                if number_arr[i]==1:
                    opCount+=1
                    number_arr[i]= 0

        return opCount





obj = Solution()
string = "100010010011110"
string = "1000101"
print obj.flipOpCount(string, 2)