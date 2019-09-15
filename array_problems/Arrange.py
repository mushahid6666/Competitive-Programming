__author__ = 'mushahidalam'


class Solution:
    # @param A : list of integers
    # Modify the array_problems A which is passed by reference.
    # You do not need to return anything in this case.
    def arrange(self, A):
        # temlist = [0 for x in range(0,n)]
        # for i in range(0,n):
        #     temlist[i] = A[A[i]]
        # return temlist
        # for i in range(0,n):
        #     A[i] = temlist[i]
        #   private static void arrange(ArrayList<Integer> a) {
        #     int n = a.size();
        #     for (int i=0;i<a.size();i++) {
        #         int x = a.get(a.get(i));
        #         int y = x%n;
        #         int z = y*n;
        #         a.set(i, a.get(i) + z);
        #     }
        #     for (int i=0;i<a.size();i++) {
        #         a.set(i, a.get(i)/n);
        #     }
        # }
        n = len(A)
        for i in range(0, n):
            x = A[A[i]]
            y = x % n
            z = y * n
            A[i] = A[i] + z
        for i in range(0, n):
            A[i] = A[i] / n


obj = Solution()
# input [2,0,1]
# output[1,2,0]
# 4 0 2 1 3

# 3 4 2 0 1
# limit:O(1) space
arr = [4, 0, 2, 1, 3]
obj.arrange(arr)
print arr
