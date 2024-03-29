"""
Patrick May
JR IS Python Timestamping Wrapper
"""

def measure_time(f):
    import time
    
    # improve stamping outfile...
    def timed(*args, **kw):
        save_to = "data\\intervals\\python\\2023-04-19 14-36-47.064445.csv"
        
        ts = time.time()
        result = f(*args, **kw)
        te = time.time()

        with open(save_to, "a") as out:
            func = f'{f.__name__}({args} kw={kw})'.replace(",","|")
            start = f'{te-ts:2.2f}\n'
            out.write(f"{func},{ts:2.4f},{te:2.4f}\n")

        return result
    return timed
