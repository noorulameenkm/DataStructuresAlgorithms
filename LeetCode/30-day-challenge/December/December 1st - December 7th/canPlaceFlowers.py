class Solution:
    def canPlaceFlowers(self, flowerbed, n):
        count = 0
        i = 0
        while i < len(flowerbed):
            if flowerbed[i] == 0 and (i == 0 or flowerbed[i - 1] == 0) and (i == len(flowerbed) - 1 or flowerbed[i + 1] == 0):
                flowerbed[i] = 1
                count += 1
                
            i += 1
            
        return count >= n


def main():
    print(Solution().canPlaceFlowers([1,0,0,0,1], 1))
    print(Solution().canPlaceFlowers([1,0,0,0,1], 2))


main()
        