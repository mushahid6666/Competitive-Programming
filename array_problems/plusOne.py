__author__ = 'mushahidalam'


class Solution:
    # @param A : list of integers
    # @return a list of integers
    def plusOne(self, A):
        carry = 1
        for i in range(len(A) - 1, -1, -1):
            if carry == 0:
                break
            if A[i] == 9:
                A[i] = 0
                carry = 1
                if i == 0:
                    A.insert(0, A[0] + 1)
                    break
            else:
                if carry == 1:
                    if A[i] == 9:
                        A[i] == 0
                        carry = 1
                        if i == 0:
                            A.append(A[0] + 1)
                            break
                        continue
                    else:
                        A[i] = A[i] + 1
                        carry = 0
                        break
                else:
                    A[i] = A[i] + 1
                    carry = 0
                    break
        B = []
        for i in range(0, len(A)):
            if A[i] == 0:
                pass
            else:
                for j in range(i, len(A)):
                    B.append(A[j])
                return B


A = Solution()
print(A.plusOne([0, 6, 0, 6, 4, 8, 8, 1]))
