class Solution:
    def nextGreatestLetter(self, letters, target):
        if target >= letters[-1]:
            return letters[0]
        
        start = 0
        end = len(letters) - 1
        letter = None
        while start <= end:
            
            # Find the mid element
            mid = start + (end - start) // 2
        
            if target < letters[mid]:
                letter = letters[mid]
                end = mid - 1
            else:
                start = mid + 1
        
        return letter




print(Solution().nextGreatestLetter(letters = ["c","f","j"], target = "a"))