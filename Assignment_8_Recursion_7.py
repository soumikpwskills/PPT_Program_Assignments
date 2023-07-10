def decodeString(s):
    stack = []
    currStr = ''
    currNum = 0

    for c in s:
      if c.isdigit():
        currNum = currNum * 10 + int(c)
      else:
        if c == '[':
          stack.append((currStr, currNum))
          currStr = ''
          currNum = 0
        elif c == ']':
          prevStr, num = stack.pop()
          currStr = prevStr + num * currStr
        else:
          currStr += c

    return currStr

s = "3[a]2[bc]"
print(decodeString(s))
