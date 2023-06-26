def check(arr):
	N = len(arr)
	inc = True
	dec = True
	
	for i in range(0, N-1):
	
		if arr[i] > arr[i+1]:
			inc = False

	for i in range(0, N-1):
	
		if arr[i] < arr[i+1]:
			dec = False

	return inc or dec

nums = [1,2,2,3]
print(check(nums))
