def findDifference(nums1, nums2):
    set1 = set(nums1)
    set2 = set(nums2)
    return [set1 - set2, set2 - set1]

if __name__ == "__main__":
    nums1 = [1,2,3]
    nums2 = [2,4,6]
    print(findDifference(nums1, nums2))