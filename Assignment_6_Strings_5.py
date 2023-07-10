def minProductSum(nums1,nums2):
    nums1.sort()
    nums2.sort()
    n, res = len(nums1), 0
    for i in range(n):
        res += nums1[i] * nums2[n - i - 1]
    return res

nums1 = [5,3,4,2]
nums2 = [4,2,2,5]
print(minProductSum(nums1,nums2))