"""
In CMD:

PowerLog.exe [-resolution <msec>] [-verbose] [-file <logfile>] -cmd {command to evaluate here}
"""

power_path = "\"C:\Program Files\Intel\Power Gadget 3.6\PowerLog3.0.exe\""

import argparse
import subprocess
from datetime import datetime, date
import time


powerlogfile = f"\"data\\power-logs\\PowerLog-{str(datetime.now()).replace(':','-')}\""
parser = argparse.ArgumentParser(description="cmd line tool for measuring energy consumption while executing a program and extracting main results")
parser.add_argument('-o', '--output', dest='outfile', default=powerlogfile)
parser.add_argument('-ctype', dest="cmdtype", default='python3')
parser.add_argument('-r', '--resolution', dest='resolution', default=10)
parser.add_argument('-v', '--verbose', dest='verbose', default=False)
parser.add_argument('-t', dest="infile")

args = parser.parse_args()

comm_types={"clang":f"wsl {args.infile}", "python3":f"python {args.infile}"}
data = args.outfile

proc = f"{power_path} -resolution {args.resolution} -file {args.outfile} -cmd {comm_types[args.cmdtype]}"
print("Running command:\n",proc)

completed = subprocess.run(proc)
#print(completed.stdout)
print("Energy Measurement Complete\n")

time.sleep(1)

print("Execution Trace Profiling\n")

# Python Profiling
if args.cmdtype == 'python3':
    import pstats
    print("Python profiling...")
    stamp = str(datetime.now()).replace(':','-').replace(" ", "-")
    profilelogfile = f"data\\profiles\\profile-{stamp}.prof" #+ "\""
    trace = subprocess.run(f"python -m cProfile -o {profilelogfile} {args.infile}")
    tested = pstats.Stats(profilelogfile)
    tested.sort_stats("cumtime")
    tested.print_stats()
    print(tested.get_stats_profile())

# transition to analyze.ipynb for now


