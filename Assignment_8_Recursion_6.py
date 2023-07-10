import collections

def findAnagrams(s,p):
    ans = []
    count = collections.Counter(p)
    required = len(p)

    for r, c in enumerate(s):
      count[c] -= 1
      if count[c] >= 0:
        required -= 1
      if r >= len(p):
        count[s[r - len(p)]] += 1
        if count[s[r - len(p)]] > 0:
          required += 1
      if required == 0:
        ans.append(r - len(p) + 1)

    return ans


s = "cbaebabacd"
p = "abc"
print(findAnagrams(s,p))