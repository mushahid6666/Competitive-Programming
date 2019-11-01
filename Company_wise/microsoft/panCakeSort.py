class Solution(object):
    def pancakeSort(self, A):
        """
        :type A: List[int]
        :rtype: List[int]
        """
        res = []
        done = 0
        while sorted(A) != A:
            lstToCheck = A[0:len(A) - done]
            indOfLargest = A.index(max(lstToCheck))
            if indOfLargest != 0:
                res.append(indOfLargest + 1)
            res.append(len(A) - done)
            A = A[:indOfLargest + 1][::-1] + A[indOfLargest + 1:]
            A[:len(A) - done] = A[:len(A) - done][::-1]
            done += 1
        return res

obj = Solution()
arr = [3,2,4,1]
print obj.pancakeSort(arr)