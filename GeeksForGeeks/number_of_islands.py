def visit_land(mat,visited,l,m,row,col):
    if l < 0 or l >= row or m < 0 or m >= col:
        return
    elif mat[l][m] != 1:
        return
    elif visited[l][m]:
        return
    else:
        visited[l][m] = True

        visit_land(mat,visited,l + 1,m,row,col)
        visit_land(mat,visited,l,m + 1,row,col)
        visit_land(mat,visited,l - 1,m,row,col)
        visit_land(mat,visited,l,m - 1,row,col)
        visit_land(mat,visited,l - 1,m - 1,row,col)
        visit_land(mat,visited,l + 1,m + 1,row,col)
        visit_land(mat,visited,l + 1,m - 1,row,col)
        visit_land(mat,visited,l - 1,m + 1,row,col)



def find_number_of_islands(mat):
    row = len(mat)
    col = len(mat[0])
    visited = [[False for i in range(col)] for j in range(row)]
    islands = 0
    for l in range(row):
        for m in range(col):
            if mat[l][m] == 1 and not visited[l][m]:
                islands = islands + 1
                visit_land(mat,visited,l,m,row,col)
    
    return islands


if __name__ == '__main__':
    mat = [
            [1,1,0,0,0],
            [0,1,0,0,1],
            [1,0,0,1,1],
            [0,0,0,0,0],
            [1,0,1,0,1]
          ]

    print(find_number_of_islands(mat))