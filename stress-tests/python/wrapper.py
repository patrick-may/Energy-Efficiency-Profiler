"""
Patrick May
JR IS Python Timestamping Wrapper
"""

def measure_time(f):
    import time
    
    # subfunciton
    def timed(*args, **kw):
        save_to = "data\intervals\python\TimeLog-2023-04-24-13-24-09.541371.csv"
        
        # timestamp start, call func, timestamp end
        ts = time.time()
        result = f(*args, **kw)
        te = time.time()

        # write to file
        with open(save_to, "a") as out:
            func = f'{f.__name__}()'.replace(",","|")
            start = f'{te-ts:2.2f}\n'
            out.write(f"{func},{ts:2.4f},{te:2.4f}\n")

        return result
    return timed
