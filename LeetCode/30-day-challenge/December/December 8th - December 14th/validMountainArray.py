class Solution:
    def validMountainArray(self, arr):
        if len(arr) < 3:
            return False
        
        i = 0
        maxIndex = -1
        while i < len(arr) - 1:
            if arr[i] < arr[i + 1]:
                maxIndex = i + 1
                i += 1
            else:
                if arr[i] == arr[i + 1]:
                    return False
                
                break
        
        if maxIndex == len(arr) - 1:
            return False
        
        i = maxIndex
        while i < len(arr) - 1:
            if arr[i] > arr[i + 1]:
                i += 1
            else:
                return False
        
        return True


def main():
    print(Solution().validMountainArray([0,3,2,1]))
    print(Solution().validMountainArray([0,3]))
    print(Solution().validMountainArray([0,3,2]))
    print(Solution().validMountainArray([0,3,2,2]))

main()
        