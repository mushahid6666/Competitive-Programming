class Solution:
    # @param A : integer
    # @return a strings
    romanlist = ['I',"II","III","IV","V","VI","VII","VIII","IX","X",
                 "XX","XXX","XL","L","LX","LXX","LXXX","XC","C",
                 "CC","CCC","CD","D","DC","DCC","DCCC","CM","M"]

    def oneToHundred(self,A):
        # print(A)
        if A==0:
            return ''
        if A<10:
            return self.romanlist[A-1]
        if A==10:
            return 'X'
        i = A/10
        k = A%10
        if k!=0:
            return self.romanlist[i+8]+self.romanlist[A%10-1]
        else:
            return self.romanlist[i+8]
    def HundredToThousand(self,A):
        # print(A)
        i = A/100
        # print(self.romanlist[i+17])
        # print(self.romanlist[i+17])
        # print(self.romanlist[i+17])
        return self.romanlist[i+17]

    def intToRoman(self, A):
        A = int(A)
        # print(A)
        if A <=99:
            return self.oneToHundred(A)
        if A<=1000:
            return self.HundredToThousand(A)+self.oneToHundred(A%100)
        lt = len(self.romanlist)
        if A<=2000:
            hund = ((A-1000)/100)
            print(hund)
            if hund == 0:
                return self.romanlist[lt-1]+self.oneToHundred(A-1000-(hund*100))
            else:
                return self.romanlist[lt-1]+self.HundredToThousand(A-1000)+self.oneToHundred(A-1000-(hund*100))
        if A<=3000:
            hund = ((A-2000)/100)
            if hund==0:
                return self.romanlist[lt-1]+self.romanlist[lt-1]+self.oneToHundred(A-2000-(hund*100))
            # print(A-2000-(hund*100))
            else:
                return self.romanlist[lt-1]+self.romanlist[lt-1]+self.HundredToThousand(A-2000)+self.oneToHundred(A-2000-(hund*100))
        else:
            hund = ((A-3000)/100)
            if hund==0:
                return self.romanlist[lt-1]+self.romanlist[lt-1]+self.romanlist[lt-1]+self.oneToHundred(A-3000-(hund*100))
            else:
                return self.romanlist[lt-1]+self.romanlist[lt-1]+self.romanlist[lt-1]+self.HundredToThousand(A-3000)+self.oneToHundred(A-3000-(hund*100))

A = Solution()
B = "1001   "
# print((int(B)-2000)/100)
print A.intToRoman(B)