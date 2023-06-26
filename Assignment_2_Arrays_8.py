def smallestRange(A, K):
    MAX = max(A)-K
    MIN = min(A)+K
    difference = MAX-MIN
    if difference <0:
        return 0
    else:
        return difference


nums = [1]
k = 0
print(smallestRange(nums,k))