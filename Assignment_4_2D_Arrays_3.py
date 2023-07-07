def transpose(mat):
    result = [[0,0,0],[0,0,0,],[0,0,0]]
    for i in range(len(mat)):
        for j in range(len(mat[0])):
            result[j][i] = mat[i][j]
    
    return result

if __name__ == "__main__":
    matrix = [[1,2,3],[4,5,6],[7,8,9]]
    print(transpose(matrix))