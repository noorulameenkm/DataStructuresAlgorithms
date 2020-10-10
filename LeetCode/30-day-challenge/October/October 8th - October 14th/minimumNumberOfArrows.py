class Solution:
    def findMinArrowShots(self, points):
        if len(points) == 0:
            return 0
        if len(points) == 1:
            return 1
        
        points.sort(key=lambda x: x[1])
        
        start, end, arrows = points[0][0], points[0][1], 1
        
        for i in range(1, len(points)):
            point = points[i]
            
            if end < point[0]:
                arrows += 1
                
                start = point[0]
                end = point[1]
            else:
                pass
            
        return arrows

print(Solution().findMinArrowShots([[10,16],[2,8],[1,6],[7,12]]))