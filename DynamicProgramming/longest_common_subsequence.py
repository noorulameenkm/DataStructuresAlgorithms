def maximum(a,b):
    return a if a > b else b

def LCS(x,y,x_length,y_length):
    table = [[0 for i in range(x_length + 1)] for j in range(y_length + 1)]
    for i in range(y_length + 1):
        for j in range(x_length + 1):
            if i == 0 or j == 0:
                table[i][j] = 0
            elif y[i-1] == x[j-1]:
                table[i][j] = table[i - 1][j - 1] + 1
            else:
                table[i][j] = maximum(table[i - 1][j],table[i][j - 1])

    return table[y_length][x_length]

def Main():
    x = input()  
    y = input()
    print("LCS is", LCS(x,y,len(x),len(y)))


if __name__ == '__main__':
    Main()


"""
    While Filling the table each cell means we are considering
    strings till that cell, if the last character matches
    then cell value will be 1 + LCS(removing that char from
    string1, removing that char from string2)(which means looking
    into the diagonal cell [i-1][j-1]), if the last character
    doesn't match then the cell value is maximum(LCS(removing
    not matching char from string1, not removing any char from string2)
    ,LCS(not removing any char from string1, removing
    not matching char from string2))(which means the max([i][j-1],[i-1][j]))
"""
