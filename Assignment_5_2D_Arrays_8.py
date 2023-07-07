import collections
def findOriginalArray(changed):
    ans = []
    q =collections.deque()

    for num in sorted(changed):
      if q and num == q[0]:
        q.popleft()
      else:
        q.append(num * 2)
        ans.append(num)

    return [] if q else ans

changed = [1,3,4,2,6,8]
print(findOriginalArray(changed))
