
def findMissingRanges(nums, lower, upper):
    nums[:] = [lower-1] + nums + [upper+1]
    res = []
    prev = nums[0]
    for curr in nums[1:]:
        if prev == curr-2:
            res.append("["+str(prev+1)+ " " + str(prev+1)+"]")
        elif prev < curr-2:
            res.append("["+str(prev+1)+ " " + str(curr-1)+"]")

        prev = curr
    return res


if __name__ == "__main__":
    nums = [0,1,3,50,75]
    lower = 0
    upper = 99
    print(findMissingRanges(nums,lower,upper))
