import random

class Uber:
    """
        Time Complexity - O(n)
        Space Complexity - O(n)
    """
    def __init__(self, metrics):
        self.metrics = metrics
        self.running_sum = [0] * len(metrics)
        self.running_sum[0] = self.metrics[0]
        for i in range(1, len(metrics)):
            self.running_sum[i] = self.running_sum[i - 1] + self.metrics[i]
        self.total_sum = self.running_sum[len(self.metrics) - 1]
    
    """
        Time Complexity - O(logn)
        Space Complexity - O(1)
    """
    def pick_route(self):
        target = self.running_sum[-1] * random.random()
        low = 0
        high = len(self.running_sum)
        while low < high:
            mid = low + (high - low) // 2

            if self.running_sum[mid] > target:
                high = mid
            else:
                low = mid + 1

        return low



# Driver code
uber = Uber([1, 2, 3])

for i in range(10):
    print("Randomly choose route", uber.pick_route())