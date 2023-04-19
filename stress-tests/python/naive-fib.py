# Patrick May, Energy Profiling Stress Tests Algorithm Analysis (c 2023)
# Find the nth fibonacci number without any optimizations

import sys
from wrapper import measure_time

@measure_time
def fib(n):
    if n == 0 or n == 1:
        return 1

    return fib(n - 1) + fib(n - 2)

sys.setrecursionlimit(10**6)
print(fib(10))
