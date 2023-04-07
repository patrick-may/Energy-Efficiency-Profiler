# from stack overflow...
def measure_time(f):
    import time
    #print("hi")
    def timed(*args, **kw):
        save_to = "data\\intervals\\temp.csv"
        ts = time.time()
        result = f(*args, **kw)
        te = time.time()

        with open(save_to, "a") as out:
            out.write(f'{f.__name__}({args} kw={kw}), {te-ts:2.2f}\n')

        return result

    return timed


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
