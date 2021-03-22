class Solution:    
    def fractionalknapsack(self, W,Items,n):
        '''
        :param W: max weight which can be stored
        :param Items: List contianing Item class objects as defined in driver code, with value and weight
        :param n: size of Items
        :return: Float value of max possible value, two decimal place accuracy is expected by driver code
        
        {
            class Item:
            def __init__(self,val,w):
                self.value = val
                self.weight = w
        }
        '''
        # code here
        for item in Items:
            item.valuePerWeight = item.value / item.weight
        
        Items.sort(key=lambda x: x.valuePerWeight, reverse=True)
        profits = 0.00
        for item in Items:
            if item.weight <= W:
                profits += item.value
                W -= item.weight
            else:
                profits += item.valuePerWeight * W
                W -= W
        
        return profits


class Item:
    def __init__(self, val, w):
        self.value = val
        self.weight = w
    
def main():
    # Test Case 1:-
    items = [Item(60, 10), Item(100, 20), Item(120, 30)]
    print(Solution().fractionalknapsack(50, items, 3))

    # Test Case 2:-
    items = [Item(60, 10), Item(100, 20)]
    print(Solution().fractionalknapsack(50, items, 2))


main()