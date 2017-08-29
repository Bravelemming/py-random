def max_sum(arr):
	max_sum = 0
	for i in range(len(arr)):
		s = 0
	for j in range (i, len(arr)):
		s += arr[j]
	if s > max_sum:
		max_sum = s
	return max_sum

# In a sequence, returns the largest total