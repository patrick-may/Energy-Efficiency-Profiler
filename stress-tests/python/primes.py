# Patrick May, Energy Profiling Stress Tests Algorithm Analysis (c 2023)
# calculate all the primes in the range of 2-1 million

import math
def gen_primes(n):
    p = []
    for i in range(2, n):
        prime = True
        for divisor in range(2, math.ceil(math.sqrt(i))):
            if i % divisor == 0:
                prime = False
        if prime:
            p.append(i)
    #print(p)

gen_primes(100_000)