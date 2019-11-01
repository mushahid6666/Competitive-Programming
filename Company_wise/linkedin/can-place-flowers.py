class Solution(object):
    def canPlaceFlowers(self, flowerbed, n):
        """
        :type flowerbed: List[int]
        :type n: int
        :rtype: bool
        """
        emptySpots = 0

        arrLength = len(flowerbed)
        if arrLength==1:
            if flowerbed[0] == 0 and n <=1:
                return True
            elif n ==0:
                return True
            return False
        i = 0
        while i < arrLength:
            if flowerbed[i]==1:
                i+=1
                continue
            if i-1>=0 and i+1 < arrLength:
                if flowerbed[i-1] == 0 and flowerbed[i+1]== 0:
                    emptySpots +=1
                    i+=2
                else:
                    i+=1
            elif i-1>=0:
                if flowerbed[i-1]==0:
                    emptySpots+=1
                    i+=2
                else:
                    i+=1
            elif i+1 < arrLength:
                if flowerbed[i+1]==0:
                    emptySpots+=1
                    i+=2
                else:
                    i+=1
        if n <= emptySpots:
            return True
        return False

obj = Solution()
# flowerbed = [0,1,0]
# n = 1
# print obj.canPlaceFlowers(flowerbed, n)
# flowerbed = [1,0,0,0,1]
# n = 1
# print obj.canPlaceFlowers(flowerbed, n)
# flowerbed = [1,0,0,0,0,1]
# n = 2
# print obj.canPlaceFlowers(flowerbed, n)
# flowerbed = [1]
# n = 2
# print obj.canPlaceFlowers(flowerbed, n)
# flowerbed = [0]
# n = 1
# print obj.canPlaceFlowers(flowerbed, n)
flowerbed = [1,0,1,0,0]
n = 1
print obj.canPlaceFlowers(flowerbed, n)
flowerbed = [0,1,0,1,0,1,0,0]
n = 1
print obj.canPlaceFlowers(flowerbed, n)
