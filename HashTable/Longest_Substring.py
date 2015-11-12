__author__ = 'mushahidalam'
class Solution:
    # @param A : string
    # # @return an integer
    # def hash(self,str1):
    #     hashvalue=0
    #     for i in range(0,len(str1)-1):
    #             hashvalue+=ord(str1[i])
    #     return hashvalue

    def lengthOfLongestSubstring(self, A):
        hashtable={}
        if len(A)==1:
            return 1
        maxsub = 0
        count = 0
        substrstart = 0
        for i in range(0,len(A)):
            hashval= A[i]
            if hashval not in hashtable:
                hashtable[hashval]= [i]
                count =i - substrstart+1
                # print(count)
            else:
                # print(int(hashtable[hashval][0]),i)
                if int(hashtable[hashval][0])>=substrstart:
                    substrstart=int(hashtable[hashval][0])+1
                    hashtable[hashval]=[i]
                    # print(substrstart)
                    if count > maxsub:
                        # print(count)
                        maxsub=count
                        count =i - substrstart+1
                        # print(count)
                    else:
                        count =i - substrstart+1
                        # print(count)
                else:
                    # print("coming here")
                    hashtable[hashval]=[i]
                    count+=1

        if count > maxsub:
            return count
        else:
            return maxsub


A = Solution()
print A.lengthOfLongestSubstring('aaaa')
