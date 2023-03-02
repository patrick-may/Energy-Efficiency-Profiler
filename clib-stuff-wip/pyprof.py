import pyRAPL
import math

pyRAPL.setup()

csv_output = pyRAPL.outputs.CSVOutput('result.csv')

@pyRAPL.measureit(output = csv_output)
def gen_primes(n):
    p = []
    for i in range(2, n):
        prime = True
        for divisor in range(math.sqrt(i)):
            if i % divisor == 0:
                prime = False
        if prime:
            p.append(i)
    print(p)

for _ in range(1):
    gen_primes(1000)

