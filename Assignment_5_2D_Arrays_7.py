import sys
def findMin(arr):
    n = len(arr) 
    mini = sys.maxsize
    for i in range(n):
        mini = min(mini, arr[i])
    return mini

if __name__ == "__main__":
    arr = [3,4,5,1,2]
    print(findMin(arr))