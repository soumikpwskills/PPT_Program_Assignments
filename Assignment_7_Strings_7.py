def backspaceCompare(s,t):
    def backspace(s):
      stack = []
      for c in s:
        if c != '#':
          stack.append(c)
        elif stack:
          stack.pop()
      return stack

    return backspace(s) == backspace(t)

s = "ab#c"
t = "ad#c"
print(backspaceCompare(s,t))