from wrapper import measure_time

def thrash():
    counter = 0
    while counter < 10_000_000:
        counter += 1
    counter = 0


def turbo_thrash():
    import threading

    for c in range(16):
        threading.Thread(thrash())


def think():
    from time import sleep
    sleep(10)


import time
ts = time.time()
for _ in range(10):
    turbo_thrash() if _ % 2 else think()
print (time.time()-ts)