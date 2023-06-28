def searchInsert(nums,target):
    left, right = 0, len(nums)
    while left < right:
        mid = (left + right) >> 1
        if nums[mid] >= target:
            right = mid
        else:
            left = mid + 1
    return left


if __name__ == "__main__":
    nums = [1,3,5,6]
    target = 5
    print(searchInsert(nums,target))