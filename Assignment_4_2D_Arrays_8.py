def shuffle(nums, n):
    result=[]
    for i in range(n):
        result+=[nums[i]]+[nums[i+n]]
    return result

nums = [2,5,1,3,4,7]
n = 3
print(shuffle(nums,n))