def sieve(n):
	loops = 0
	numbers = set(range(2, n))
	for i in range(2, int(n**0.5)+1):
		for j in range(i*2, n, i):
			numbers.discard(j)
			loops += 1
	return sorted(numbers), loops

# n = int(input('enter the range: '))
print(sieve(1000))

