def singleNumber(nums):
    count = 0
    for i in nums:
        count = count^i
    return count


if __name__ == "__main__":
    nums  = [2,2,1]
    print(singleNumber(nums))