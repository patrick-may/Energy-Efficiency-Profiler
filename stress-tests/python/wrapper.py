# from stack overflow...
def measure_time(f):
    import time
    # improve stamping outfile...
    def timed(*args, **kw):
        save_to = "data\\intervals\\temp1.csv"
        ts = time.time()
        result = f(*args, **kw)
        te = time.time()

        with open(save_to, "a") as out:
            out.write(f'{f.__name__}({args} kw={kw}), {te-ts:2.2f}\n')

        return result

    return timed
