def SortedSquares (arr):
    temp = [x**2 for x in arr]
    return sorted(temp)

nums = [-4,-1,0,3,10]
print(SortedSquares(nums))