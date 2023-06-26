import collections

def findLHS(nums):
    ans = 0
    count = collections.Counter(nums)

    for num, freq in count.items():
      if num + 1 in count:
        ans = max(ans, freq + count[num + 1])

    return ans

nums = [1,3,2,2,5,2,3,7]
print(findLHS(nums))