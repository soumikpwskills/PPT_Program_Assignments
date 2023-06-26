def arrayPairSum(nums):
    nums_sort = sorted(nums)
    res = 0
    i = 0
    while i < len(nums):
        res += nums_sort[i]
        i += 2
    return res

nums = [1,4,3,2]
print(arrayPairSum(nums))