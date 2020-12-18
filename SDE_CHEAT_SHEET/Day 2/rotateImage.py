def rotateImage(matrix):
    n = len(matrix)
    result = [[0 for _ in range(n)] for _ in range(n)]

    for i in range(n):
        for j in range(n):
            result[i][j] = matrix[n - j - 1][i]
    
    return result


def rotateImage2(matrix):
    n = len(matrix)

    for i in range(n):
        for j in range(i):
            matrix[i][j], matrix[j][i] = matrix[j][i], matrix[i][j]
    
    for i in range(n):
        matrix[i][0:] = matrix[i][::-1]
    
    return matrix


def rotateImage3(A):
    N = len(A)
    for i in range(N // 2):
        for j in range(i, N - i - 1):
            temp = A[i][j]
            A[i][j] = A[N - 1 - j][i]
            A[N - 1 - j][i] = A[N - 1 - i][N - 1 - j]
            A[N - 1 - i][N - 1 - j] = A[j][N - 1 - i] 
            A[j][N - 1 - i] = temp
    return A

def main():
    # First Aproach
    print(rotateImage([[1,2,3],[4,5,6],[7,8,9]]))

    # Second Aproach
    print(rotateImage2([[1,2,3],[4,5,6],[7,8,9]]))

    # Third Aproach
    print(rotateImage3([[1,2,3],[4,5,6],[7,8,9]]))

main()