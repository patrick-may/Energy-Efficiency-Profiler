from wrapper import measure_time

def thrash():
    counter = 0
    while counter < 10_000_000:
        counter += 1

@measure_time
def turbo_thrash():
    import threading

    for c in range(10):
        threading.Thread(thrash())

@measure_time
def think():
    from time import sleep
    sleep(10)

for _ in range(10):
    turbo_thrash() if _ % 2 else think()
