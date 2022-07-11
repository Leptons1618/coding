# algorithm Sieve of Eratosthenes is
#     input: an integer n > 1.
#     output: all prime numbers from 2 through n.

#     let A be an array of Boolean values, indexed by integers 2 to n,
#     initially all set to true.
    
#     for i = 2, 3, 4, ..., not exceeding √n do
#         if A[i] is true
#             for j = i2, i2+i, i2+2i, i2+3i, ..., not exceeding n do
#                 A[j] := false

#     return all i such that A[i] is true.


def sieve_eratosthenes(n):
    loops = 0
    primes = set(range(2,n))
    for i in range(2, int(n**0.5)+1):
        for j in range(i*2, n, i):
            primes.discard(j)
            loops += 1
    return sorted(primes),loops

n = int(input('prime numbers upto: '))
print(sieve_eratosthenes(n))