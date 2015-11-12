__author__ = 'mushahidalam'
class Solution:
    # @param A : tuple of strings
    # @return a list of list of integers
    def hash(self,str1):
        hashvalue=0
        for i in range(0,len(str1)-1):
                hashvalue+=ord(str1[i])
        return hashvalue

    def anagrams(self, A):
        hashtable = {}
        result = []
        id=0
        for str1 in A:
            hashval = self.hash((str1))
            if hashval not in hashtable:
                hashtable[hashval]= [id+1]
            else:
                hashtable[hashval].append(id+1)
            id+=1
        for i in hashtable:
            result.append(hashtable[i])
        return result






A = Solution()
B = ("abcd",'$12#' )
print(A.anagrams(B))