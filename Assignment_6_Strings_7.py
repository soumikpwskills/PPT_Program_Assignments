def generateMatrix(n):
    row1 = 0
    col1 = 0
    row2 = n
    col2 = n
    result = [ [0 for i in range(n)] for j in range(n)]
    num = 1
    while num<=n**2:
        for i in range(col1,col2):
            result[row1][i] = num
            num+=1
        if num > n**2:
            break
        for i in range(row1+1,row2):
            result[i][col2-1] = num
            num+=1
        if num > n**2:
            break
        for i in range(col2-2,col1-1,-1):
            result[row2-1][i] = num
            num+=1
        if num > n**2:
            break
        for i in range(row2-2,row1,-1):
            result[i][col1] = num
            num+=1
            row1+=1
            row2-=1
            col1+=1
            col2-=1
    return result


n = 3
print(generateMatrix(n))