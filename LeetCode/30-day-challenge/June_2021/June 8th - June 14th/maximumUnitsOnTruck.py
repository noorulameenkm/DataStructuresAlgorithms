from typing import List

class Solution:
    def maximumUnits(self, boxTypes: List[List[int]], truckSize: int) -> int:
        boxTypes.sort(key=lambda box: -box[1])
        max_units = 0
        box_taken = 0
        for i in range(len(boxTypes)):
            if box_taken == truckSize:
                return max_units
            
            box = boxTypes[i]
            
            if truckSize - box_taken <= box[0]:
                max_units += ((truckSize - box_taken) * box[1])
                box_taken += (truckSize - box_taken)
            else:
                max_units += (box[0] * box[1])
                box_taken += box[0]
        
        return max_units
        


print(Solution().maximumUnits(boxTypes = [[1,3],[2,2],[3,1]], truckSize = 4))
print(Solution().maximumUnits(boxTypes = [[5,10],[2,5],[4,7],[3,9]], truckSize = 10))