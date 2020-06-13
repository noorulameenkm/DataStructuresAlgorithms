import random

class RandomizedSet:

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.random_set = []
        self.index_store = {}

    def insert(self, val: int) -> bool:
        """
        Inserts a value to the set. Returns true if the set did not already contain the specified element.
        """
        if val in self.index_store:
            return False
        
        self.random_set.append(val)
        self.index_store[val] = len(self.random_set) - 1
        return True

    def remove(self, val: int) -> bool:
        """
        Removes a value from the set. Returns true if the set contained the specified element.
        """
        if val in self.index_store:
            index = self.index_store[val]
            last_element = self.random_set[-1]
            self.random_set[index], self.index_store[last_element] = last_element, index
            del self.index_store[val]
            self.random_set.pop()
            return True
        
        return False

    def getRandom(self) -> int:
        """
        Get a random element from the set.
        """
        return random.choice(self.random_set)
        


# Your RandomizedSet object will be instantiated and called as such:
obj = RandomizedSet()
print(f'Answer is {obj.insert(1)}')
print(f'Answer is {obj.remove(2)}')
print(f'Answer is {obj.getRandom()}')
