"""
Patrick May
JR IS Python Timestamping Wrapper
"""

def measure_time(f):
    import time
    
    # improve stamping outfile...
    def timed(*args, **kw):
        save_to = "data\\intervals\\python\\2023-04-19 12-59-49.133508.csv"
        ts = time.time()
        result = f(*args, **kw)
        te = time.time()

        with open(save_to, "a") as out:
            func = f'{f.__name__}({args} kw={kw})'.replace(",","|")
            stamp = f'{te-ts:2.2f}\n'
            out.write(f"{func},{stamp}")

        return result

    return timed
