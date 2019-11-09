def findmax(a, b):
    return a if a > b else b

def knapsack(W, wt, val, n):

    """ 
        if Capacity or number of elements(n) is 0, then return 0
    """
    if W == 0 or n == 0:
        return 0

    """ 
        if the weight of the last element is greater than
        the total capacity of the knapsack, then return the 
        result of the knapsack function without including the last
        element.
    """  
    if wt[n - 1] > W:
        return knapsack(W, wt, val, n - 1)

    return findmax(
                    val[n - 1] + knapsack(W - wt[n - 1], wt, val, n - 1),
                    knapsack(W,wt,val,n - 1)
                  )


def Main():
    n,capacity = [int(num) for num in input().split(" ") if num != '']
    object_values = [int(value) for value in input().split(" ") if value != '']
    object_weights = [int(weight) for weight in input().split(" ") if weight != '']
    print(knapsack(capacity, object_weights, object_values, n))

if __name__ == '__main__':
    Main()