class Solution:
    # @param A : integer
    # @return a strings
    def countAndSay(self, A):
        one = "11"
        two = "12"
        twoones = "21"
        twofollwedone = "1211"
        __list = ['1',one,twoones,twofollwedone]
        if A == 1:
            return __list[0]
        if A == 2:
            return __list[1]
        if A == 3:
            return __list[2]
        if A==4:
            return __list[3]
        for i in range(3,A-1):
            temp = __list[i]
            # print(i,A-1)
            gen = ''
            for i in range(0,len(temp)):
                if i >= len(temp):
                    continue
                print(temp[i])
                if temp[i]=='1':
                    try:
                        if temp[i+1]=='1':
                            gen = gen+twoones
                        else:
                            gen = gen+one
                        i+=1
                        print(gen)
                        continue
                    except:
                        continue
                if temp[i]=='2':
                    try:
                        if temp[i+1]=='1':
                            gen = gen+twofollwedone
                        else:
                            gen = gen+two
                        i+=1
                        print(gen)
                        continue
                    except:
                        continue
            # print(gen)


A = Solution()
# print((int(B)-2000)/100)
print A.countAndSay(5)
