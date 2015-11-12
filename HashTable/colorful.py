__author__ = 'mushahidalam'
class Solution:
    # @param A : integer
    # @return an integer
    def colorful(self, A):
        hastable = {}
        sum=1
        num = str(A)
        size =1
        while size <=len(num):
            for j in range(0,len(num)):
                if j+size > len(num):
                    break
                key = num[j:j+size]
                print(key)
                for i in range(0,size):
                    sum*=int(key[i])
                if sum in hastable:
                    return 0
                else:
                    hastable[sum] = key
                sum=1
            size+=1
        return 1

A = Solution()
B = 123
print(A.colorful(B))
