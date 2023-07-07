def arrangeCoins(n):
    level = 0
    coin = 1
    while (n >= coin):
        n = n-coin
        coin = coin+1
        level = level+1
    return level

n = 5
print(arrangeCoins(n))