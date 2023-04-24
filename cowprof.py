"""
Patrick May
JR IS Energy Profiling Energy Script

Current Measurement Tool is Intel's PowerLog3.0. That Works in Windows CMD.
Invoked with:

PowerLog.exe [-resolution <msec>] [-verbose] [-file <logfile>] -cmd {command to evaluate here}
"""

import argparse
import subprocess
from datetime import datetime, date
import time

# the CMD path to your installed PowerLog3.0
power_path = "\"C:\Program Files\Intel\Power Gadget 3.6\PowerLog3.0.exe\""

def cplusplus():
    # c++ prof time
    print("C Plus Plus Profiler 😼")

    # uh linux based file pathing for wsl exec
    timepath = f"data/intervals/c++/TimeLog-{ts}.csv"
    full_line = f"#define COWPROF_FILEPATH \"{timepath}\"\n"

    # similar c++ wrapper rewrite fn
    with open("stress-tests\\c++\\wrapper.hpp") as dec:
        full = dec.readlines()

    # filter entire file (its a short wrapper file)
    updated = []
    for line in full:
        if "#define COWPROF_FILEPATH" in line:
            updated.append(full_line)
        else:
            updated.append(line)

    # rewrite entire wrapper file 
    with open("stress-tests\\c++\\wrapper.hpp", "w") as dec:
        dec.writelines(updated)
    
    # open timings file and initialize proper headers
    with open(timepath.replace("/", "\\"), "a") as logfile:
        logfile.write("func-head,start,end\n")

    # our subprocess compile command
    proc = f"{power_path} -resolution {args.resolution} -file {args.outfile} -cmd {comm_types[args.cmdtype]}"
    print("Running command:\n",proc)

    # run command and print its output
    completed = subprocess.run(proc,capture_output=True)
    print(completed.stdout)
    print("\nC++ Compilation Complete\n")

    time.sleep(3)

    # run the compiled script
    proc = f"{power_path} -resolution {args.resolution} -file {args.outfile} -cmd wsl ./a.out"
    print("\nExecuting Code\n")
    completed = subprocess.run(proc,capture_output=True)
    print(completed.stdout)
    from analyze import analyze    
    analyze(pdata=f"{args.outfile}", tdata=timepath)


def pyprof():
    # pyprof time
    print("Python Profiling 🗿")

    # first edit the 'wrapper' output file (this is a bit of a hack)
    # the leading whitespace is MANDATORY. And may or may not be compatible with your current configuration
    # oopsies

    timepath = f"data\\intervals\\python\\TimeLog-{ts}.csv"
    full_line = f"        save_to = \"{timepath}\"\n"
    
    # read in file
    with open("stress-tests\\python\\wrapper.py") as dec:
        full = dec.readlines()

    # filter entire file (its a short wrapper file)
    updated = []
    for line in full:
        if "save_to = " in line:
            updated.append(full_line)
        else:
            updated.append(line)

    # rewrite entire wrapper file 
    with open("stress-tests\\python\\wrapper.py", "w") as dec:
        dec.writelines(updated)
    
    with open(timepath.replace("\\\\", "\\").replace("\"", ""), "a") as logfile:
        logfile.write("func-head,start,end\n")

    # our subprocess ommand
    proc = f"{power_path} -resolution {args.resolution} -file {args.outfile} -cmd {comm_types[args.cmdtype]}"
    print("Running command:\n",proc)

    # compile the command
    completed = subprocess.run(proc)
    print(completed.stdout)
    print("\nExecution Complete\n")

    time.sleep(1)
    from analyze import analyze
    
    analyze(pdata=f"{args.outfile}", tdata=timepath)
    
# datetime ts
ts = str(datetime.now()).replace(':','-').replace(" ", "-")
powerlogfile = f"data\\power-logs\\PowerLog-{ts}"

# argparse stuff
parser = argparse.ArgumentParser(description="cmd line tool for measuring energy consumption while executing a program and extracting main results")
parser.add_argument('-o', '--output', dest='outfile', default=powerlogfile)
parser.add_argument('-ctype', dest="cmdtype", default='python3')
parser.add_argument('-r', '--resolution', dest='resolution', default=10)
parser.add_argument('-v', '--verbose', dest='verbose', default=False)
parser.add_argument('-t', dest="infile")
args = parser.parse_args()

comm_types={"c++":f"wsl {args.infile}", "python3":f"python {args.infile}"}
data = args.outfile

print("Execution Trace Profiling\n")

# call the different functions to handle specific language profiling
if args.cmdtype == 'python3':
    pyprof()
if args.cmdtype == 'c++':
    cplusplus()



