def distributeCandies(candyType):
    return min(len(candyType) >> 1, len(set(candyType)))


candyType = [1,1,2,2,3,3]
print(distributeCandies(candyType))