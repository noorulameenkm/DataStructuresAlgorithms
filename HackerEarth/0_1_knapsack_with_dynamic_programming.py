def findMax(a, b):
    return a if a > b else b


def knapsack(W, wt, val, n):
    table = [[0 for k in range(W + 1)] for l in range(n + 1)]

    for i in range(n + 1):
        for j in range(W + 1):

            """
                The entire 0th column and 0th row should be 0
            """
            if i == 0 or j == 0:
                table[i][j] = 0

            elif wt[i - 1] <= j:
                table[i][j] = findMax(val[i - 1] + table[i - 1][j - wt[i - 1]], table[i - 1][j])

            else:
                table[i][j] = table[i - 1][j]

    return table[n][W]


def Main():
    n, capacity = [int(num) for num in input().split(" ") if num != '']
    object_values = [int(value) for value in input().split(" ") if value != '']
    object_weights = [int(weight) for weight in input().split(" ") if weight != '']
    print(knapsack(capacity, object_weights, object_values, n))


if __name__ == '__main__':
    Main()

    """ 
        The weight of the selected object is less than the
        capacity of the current bag then, the max value will be
        the max(maxValue without including the current object with
        the same capacity and value of current selected object plus
        the maxValue before adding current selected object for the bag of
        capacity(current bag capacity minus the weight of the current
        weight of the object))
    """