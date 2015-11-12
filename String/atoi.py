class Solution:
    # @param str : string
    # @return an integer
    def atoi(self, str):
        numstr = ''
        flag = 0
        firstdigit = 0
        str = str.strip()
        for i in range(0,len(str)):
            if firstdigit==0 and str[i]=='-':
                if str[i+1].isdigit():
                    numstr=numstr+str[i]
                    continue
                else:
                    return 0
            if firstdigit==0 and str[i].isalpha():
                return 0
            if firstdigit==0 and str[i]=='+' and str[i+1].isspace():
                return 0
            if flag==1:
                if str[i].isspace() or str[i].isalpha():
                    break
            if str[i].isdigit():
                if flag==0:
                    flag=1
                    firstdigit=1
                numstr = numstr+str[i]
        # #print(int(numstr))
        if len(numstr)!=1:
            numstr = numstr.lstrip('0')
        if numstr[0]=='-':
            lt = len(numstr)
            for i in range(1,lt):
                try:
                    #print(i,numstr[i])
                    if numstr[i]=='0':
                        numstr=numstr.replace('0','',i)
                        if numstr[i]!='0':
                            break
                    else:
                        break
                except:
                    break
        # #print(numstr)

        if int(numstr) > 2147483647:
            if int(numstr) > 0:
                return 2147483647
            else:
                return 1
        if int(numstr) < -2147483647:
            return -2147483647
        return numstr
        # #print(numstr)


str = Solution()
#print str.atoi("  + 3611156")

