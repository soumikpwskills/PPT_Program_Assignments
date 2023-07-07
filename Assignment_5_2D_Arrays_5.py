def findTheDistanceValue(arr1, arr2, d):
    res = 0
    for x in arr1:
        cnt = 0
        for y in arr2:
            if abs(x-y) <= d:
                break
            else:
                cnt += 1
            if cnt == len(arr2):
                res += 1
    return res

    return sum(all(abs(a1 - a2) > d for a2 in arr2) for a1 in arr1)

if __name__ == "__main__":
    arr1 = [4,5,8]
    arr2 = [10,9,1,8]
    d = 2
    print(findTheDistanceValue(arr1, arr2, d))