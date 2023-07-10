def findOriginal(arr):
	numFreq = {}

	for i in range(0, len(arr)):
		if (arr[i] in numFreq):
			numFreq[arr[i]] += 1
		else:
			numFreq[arr[i]] = 1

	arr.sort()

	res = []

	for i in range(0, len(arr)):
	
		freq = numFreq[arr[i]]
		if (freq > 0):
			res.append(arr[i])
			numFreq[arr[i]] -= 1

			twice = 2 * arr[i]

			numFreq[twice] -= 1

	return res

changed = [1,3,4,2,6,8]
print(findOriginal(changed))

