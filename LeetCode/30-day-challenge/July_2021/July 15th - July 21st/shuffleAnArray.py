"""
    Problem Link:- https://leetcode.com/problems/shuffle-an-array/
    Algorithm:- Fisher–Yates shuffle
"""

import random
class Solution:

    def __init__(self, nums):
        self.nums = nums

    def reset(self):
        """
        Resets the array to its original configuration and return it.
        """
        return self.nums

    def shuffle(self):
        """
        Returns a random shuffling of the array.
        """
        randomArray = list(self.nums)
        length = len(randomArray)
        for i in range(length - 1, -1, -1):
            randomIndex = random.randint(0, i)
            copy = randomArray[i]
            randomArray[i] = randomArray[randomIndex]
            randomArray[randomIndex] = copy
        
        return randomArray



