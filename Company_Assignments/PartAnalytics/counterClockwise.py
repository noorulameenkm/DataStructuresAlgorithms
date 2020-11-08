
# function to check whether to exit out of the loop
def checkEndCondition(start, end):
    return start > end




"""
Time Complexity - O(m * n)
Space complexity - O(m * n) -> for the matrix
"""

def print_counter_clockwise(m, n):
    # initialise matrix
    matrix = [[0 for i in range(n)] for j in range(m)]

    # initialize variables
    startNumber = 1 # starting number (always 1)
    endNumber = m * n # ending number (rows * cols)
    startRow, endRow = 0, m - 1 
    startCol, endCol = n - 1, 0

    while (startRow <= endRow or startCol >= endCol):
        # for the first row (right to left)   
        for j in range(startCol, endCol - 1, -1):
            matrix[startRow][j] = startNumber
            startNumber += 1

        # increase the first row pointer
        startRow += 1

        if checkEndCondition(startNumber, endNumber):
            break

        # for the first column (top to bottom)
        for i in range(startRow, endRow + 1):
            matrix[i][endCol] = startNumber
            startNumber += 1 
        
        # increase the first column pointer 
        endCol += 1

        if checkEndCondition(startNumber, endNumber):
            break

        # for the last row (left to right)
        for j in range(endCol, startCol + 1):
            matrix[endRow][j] = startNumber
            startNumber += 1
        
        # decrease the last row pointer
        endRow -= 1

        if checkEndCondition(startNumber, endNumber):
            break

        # for the last column (bottom to top)
        for i in range(endRow, startRow - 1, -1):
            matrix[i][startCol] = startNumber
            startNumber += 1


        # decrease the last column pointer
        startCol -= 1 

        if checkEndCondition(startNumber, endNumber):
            break


    # print the matrix
    print('\n'.join(['\t'.join([str(x) for x in row]) for row in matrix]))


def main():
    try:
        m = int(input('m = '))
        n = int(input('n = '))
        if m > 0 and n > 0:
            # call print_counter_clockwise
            print_counter_clockwise(m, n)
        else:
            print('m and n should be greater than 0')

    except Exception as e:
        print('Enter Valid Input')


main()