

def get_divisors(n):
	divisors = [1]
	for i in range(2, int(n/2) + 1):
		if n % i == 0:
			divisors.append(i)
		return divisors

def is_perfect(n):
	divisors = get_divisors(n)
	sum = 0
	for i in divisors:
		sum+= i
	return n == sum

print (is_perfect(6))