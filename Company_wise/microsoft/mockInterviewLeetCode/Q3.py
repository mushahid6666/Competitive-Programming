import sys, copy
class Solution(object):
    def prevPermOpt1(self, A):
        """
        :type A: List[int]
        :rtype: List[int]
        """
        if len(A)==0 or len(A)==1:
            return A
        max_numer = ["0"]
        for i in range(len(A)):
            A[i] = str(A[i])
        orig_number = int("".join(A))
        for i in range(len(A)-1):
            for j in range(i+1, len(A)):
                temp = A[i]
                A[i]= A[j]
                A[j]=temp
                newNumber = int("".join(A))
                if newNumber < orig_number:
                    cur_max = int("".join(max_numer))
                    if cur_max < newNumber:
                        max_numer = copy.deepcopy(A)
                temp = A[i]
                A[i] = A[j]
                A[j] = temp

        if len(max_numer)==1 and max_numer[0]=="0":
            return A

        return max_numer




obj = Solution()
# number = [10,2,1]
# print obj.prevPermOpt1(number)
# number = [1,1,5]
# print obj.prevPermOpt1(number)
# number = [1,9,4,6,7]
# print obj.prevPermOpt1(number)
# number = [3,1,1,3]
# print obj.prevPermOpt1(number)
number = [1,1,9,4,9,7,7,5,3,10,4,10,2,3,4,9,4,6,5,10,7,2,9,4,10,7,10,5,10,9,5,3,6,9,3,1,2,9,1,4,5,1,3,2,10,7,9,6,9,6,9,9,1,8,7,8,9,5,9,8,6,1,10,9]
print obj.prevPermOpt1(number)