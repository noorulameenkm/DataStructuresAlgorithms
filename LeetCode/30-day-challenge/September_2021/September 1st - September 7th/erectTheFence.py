"""
    Problem Link- https://leetcode.com/problems/erect-the-fence/
"""


class Solution:
    def outerTrees(self, trees):
        def compact(p1, p2, p3):
            x1, y1 = p1
            x2, y2 = p2
            x3, y3 = p3

            return (y3 - y2) * (x2 - x1) - (y2 - y1) * (x3 - x2)

        points = sorted(trees)
        upper = []
        lower = []
        for point in points:
            while len(lower) >= 2 and compact(lower[-2], lower[-1], point) > 0:
                lower.pop()

            while len(upper) >= 2 and compact(upper[-2], upper[-1], point) < 0:
                upper.pop()

            lower.append(tuple(point))
            upper.append(tuple(point))

        return list(set(lower + upper))


print(Solution().outerTrees(trees=[[1, 1], [2, 2], [2, 0], [2, 4], [3, 3], [4, 2]]))
print(Solution().outerTrees(trees=[[1, 2], [2, 2], [4, 2]]))
