def maximum(a,b):
    return a if a > b else b

def LCS(x, y, x_length,y_length):
    if x_length == 0 or y_length == 0:
        return 0
    elif x[x_length - 1] == y[y_length - 1]:
        return LCS(x,y,x_length - 1,y_length - 1) + 1
    else:
        return maximum(LCS(x,y,x_length,y_length - 1), LCS(x,y,x_length - 1,y_length))


def Main():
    x = input()
    y = input()
    print("LCS is",LCS(x,y,len(x),len(y)))  


if __name__ == '__main__':
    Main()



