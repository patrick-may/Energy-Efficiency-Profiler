from wrapper import measure_time
"""
Sieve of Erathosthenes, Slightly modified
to have more visible function calls
"""

@measure_time
def SieveOfEratosthenes(num):
    prime = [True for i in range(num+1)]

    p = 2

    
    def range_update(p, n):
        for i in range(p*p, n + 1, p):
            prime[i] = False

    while (p * p <= num):
 
        # If prime[p] is not
        # changed, then it is a prime
        if (prime[p] == True):
 
            # Updating all multiples of p
            range_update(p, num)

        p += 1
    return prime

@measure_time
def findlast():
    idx = -1
    while not primes[idx]:
        idx -=1
    print(100_000_000 + idx + 1)

primes = SieveOfEratosthenes(100_000_000)
findlast()

