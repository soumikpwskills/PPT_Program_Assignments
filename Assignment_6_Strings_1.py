def diStringMatch(s):
    ans = []
    mini = 0
    maxi = len(s)

    for c in s:
      if c == 'I':
        ans.append(mini)
        mini += 1
      else:
        ans.append(maxi)
        maxi -= 1

    return ans + [mini]

if __name__ == "__main__":
    s = "IDID"
    print(diStringMatch(s))
