def thrash():
    counter = 0
    while counter < 10_000_000:
        counter += 1
    
def think():
    from time import sleep
    sleep(10)

for _ in range(10):
    thrash() if _ % 2 else think()
