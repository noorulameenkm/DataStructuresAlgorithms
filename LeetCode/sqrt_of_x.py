class Solution:
    def mySqrt(self, x: int) -> int:
        start, end = 1, x
        if x == 0:
            return 0
        
        while start <= end:
            mid = start + (end - start) // 2
            
            # midSquare = mid * mid
            
            if square(mid) > x:
                end = mid - 1
            elif square(mid) == x or square(mid + 1) > x:
                return mid
            else:
                start = mid + 1
                
                
def square(num):
    return num * num
                
        

def main():
    print(Solution().mySqrt(5))
    print(Solution().mySqrt(9))
    print(Solution().mySqrt(8))

main()