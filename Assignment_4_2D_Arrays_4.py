def arrayPairSum(a):
    res = 0
    a = sorted(a)
    for i in range(0,len(a)-1,2):
        res += a[i]
    return res

nums = [1,4,3,2]
print(arrayPairSum(nums))