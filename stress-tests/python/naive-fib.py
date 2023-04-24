# Patrick May, Energy Profiling Stress Tests Algorithm Analysis (c 2023)
# Find the nth fibonacci number without any optimizationst

from wrapper import measure_time

@measure_time
def fib(n):
    if n == 0 or n == 1:
        return 1

    return fib(n - 1) + fib(n - 2)


n = fib(20)
print(n)
