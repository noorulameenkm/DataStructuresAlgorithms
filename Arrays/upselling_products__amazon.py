from random import choice


class UpsellProducts:
    def __init__(self):
        self.product_list = []
        self.product_dict = {}
    
    
    """
        Time Complexity - O(1) amortized
        Space Complexity - O(n)
    """
    def insertProduct(self, prod):

        if prod in self.product_dict:
            return False
        
        self.product_dict[prod] = len(self.product_list)
        self.product_list.append(prod)
    
    
    """
        Time Complexity - O(1) amortized
        Space Complexity - O(n)
    """
    def removeProduct(self, prod):

        if prod in self.product_dict:

            product, i = self.product_list[-1], self.product_dict[prod]
            self.product_list[i], self.product_dict[product] = product, i
            del self.product_dict[prod]
            self.product_list.pop()
            return True
        return False
    

    """
        Time Complexity - O(1)
        Space Complexity - O(1)
    """
    def getRandomProduct(self):
        return choice(self.product_list)



# Driver code
dataset = UpsellProducts()
dataset.insertProduct(1212)
dataset.insertProduct(190)
dataset.insertProduct(655)
dataset.insertProduct(327)
print(dataset.getRandomProduct())
dataset.removeProduct(190)
dataset.removeProduct(655)
print(dataset.getRandomProduct())
print(dataset.getRandomProduct())