import threading
def thrash():
    counter = 0
    
    while counter < 1_000_000_000:
        counter += 1
    
    exit()

for c in range(10):
    threading.Thread(thrash())
