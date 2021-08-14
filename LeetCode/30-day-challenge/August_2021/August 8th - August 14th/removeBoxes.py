"""
    Problem Link:- https://leetcode.com/problems/remove-boxes/
"""


def remove_boxes(boxes):
    dp_table = {}

    def dp(left, right, count=0):
        if left > right:
            return 0

        key = f"{left}:{right}:{count}"
        if key in dp_table:
            return dp_table[key]

        while left + 1 < right and boxes[left] == boxes[left + 1]:
            left += 1
            count += 1

        ans = (count + 1) ** 2 + dp(left + 1, right, 0)
        for m in range(left + 1, right + 1):
            if boxes[m] == boxes[left]:
                ans = max(ans, dp(m, right, count + 1) + dp(left + 1, m - 1, 0))

        dp_table[key] = ans
        return dp_table[key]

    return dp(0, len(boxes) - 1, 0)


print(remove_boxes(boxes=[1, 3, 2, 2, 2, 3, 4, 3, 1]))
print(remove_boxes(boxes=[1, 1, 1]))
print(remove_boxes(boxes=[1]))
