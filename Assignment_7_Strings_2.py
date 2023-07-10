def isStrobogrammatic(num):
      
    maps = {("0", "0"), ("1", "1"), ("6", "9"), ("8", "8"), ("9", "6")}
    i,j = 0, len(num) - 1
    while i <= j:
        if (num[i], num[j]) not in maps:
            return False
        i += 1
        j -= 1
    return True

num = "69"
print(isStrobogrammatic(num))