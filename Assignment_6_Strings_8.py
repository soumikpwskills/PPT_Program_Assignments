def multiply(mat1, mat2):
    r1, c1, c2 = len(mat1), len(mat1[0]), len(mat2[0])
    res = [[0] * c2 for _ in range(r1)]
    for i in range(r1):
        for j in range(c2):
            for k in range(c1):
                res[i][j] += mat1[i][k] * mat2[k][j]
    return res

mat1 = [[1,0,0],[-1,0,3]]
mat2 = [[7,0,0],[0,0,0],[0,0,1]]
print(multiply(mat1,mat2))