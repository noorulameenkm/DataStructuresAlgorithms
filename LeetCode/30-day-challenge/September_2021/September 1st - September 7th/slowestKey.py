"""
    Problem Link:- https://leetcode.com/problems/slowest-key/
"""


class Solution:
    def slowestKey(self, releaseTimes, keysPressed):
        ans = keysPressed[0]
        max_pressed_time = releaseTimes[0]

        for i in range(1, len(releaseTimes)):
            pressed_time = releaseTimes[i] - releaseTimes[i - 1]
            if pressed_time > max_pressed_time:
                max_pressed_time = pressed_time
                ans = keysPressed[i]
            elif pressed_time == max_pressed_time and keysPressed[i] > ans:
                ans = keysPressed[i]

        return ans


print(Solution().slowestKey(releaseTimes=[9, 29, 49, 50], keysPressed="cbcd"))
print(Solution().slowestKey(releaseTimes=[12, 23, 36, 46, 62], keysPressed="spuda"))
