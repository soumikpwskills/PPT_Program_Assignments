def minimumDeleteSum(s1, s2):
    dp = [[0] * (len(s2)+1) for _ in range(len(s1)+1)]
    for i in range(len(s1)):
        dp[i+1][0] = dp[i][0] + ord(s1[i])
    for j in range(len(s2)):
            dp[0][j+1] = dp[0][j] + ord(s2[j])

    for i in range(len(s1)):
        for j in range(len(s2)):
            if s1[i] == s2[j]:
                dp[i+1][j+1] = dp[i][j]
            else:
                dp[i+1][j+1] = min(dp[i][j+1] + ord(s1[i]), dp[i+1][j] + ord(s2[j]))

    return dp[-1][-1]

s1 = "sea"
s2 = "eat"
print(minimumDeleteSum(s1,s2))