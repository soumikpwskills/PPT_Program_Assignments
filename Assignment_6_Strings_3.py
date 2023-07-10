def isMountainArray(arr):

	if (len(arr) < 3):
		return False
	flag = 0
	i = 0
	for i in range(1, len(arr)):
		if (arr[i] <= arr[i - 1]):
			break

	if (i == len(arr) or i == 1):
		return False

	while i < len(arr):
		if (arr[i] >= arr[i - 1]):
			break
		i += 1
	return i == len(arr)


if __name__ == "__main__":

	arr = [2,1]
    
	if (isMountainArray(arr)):
		print("true")
	else:
		print("false")
