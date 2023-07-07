def convert(original,m,n):
    if m*n != len(original):
        return []
      
    ans = []
    for i in range(0, m*n, n):
        ans.append(original[i:i+n])
            
    return ans

original = [1,2,3,4]
m = 2
n = 2
print(convert(original,m,n))