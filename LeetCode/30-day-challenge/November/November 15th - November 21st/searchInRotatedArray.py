class Solution:
    def search(self, arr, target):
        start, end = 0, len(arr) - 1
        
        while start <= end:
            
            mid = start + (end - start) // 2
            
            if arr[mid] == target:
                return True
            elif arr[start] == arr[mid] and arr[mid] == arr[end]:
                start += 1
                end -= 1
            elif arr[start] <= arr[mid]:
                if target >= arr[start] and target < arr[mid]:
                    end = mid - 1
                else:
                    start = mid + 1
            else:
                if target > arr[mid] and target <= arr[end]:
                    start = mid + 1
                else:
                    end = mid - 1
                    
        return False
        

def main():
    print(Solution().search([2,5,6,0,0,1,2], 0))
    print(Solution().search([2,5,6,0,0,1,2], 3))


main()