"""
In CMD:

PowerLog.exe [-resolution <msec>] [-verbose] [-file <logfile>] -cmd {command to evaluate here}
"""

power_path = "\"C:\Program Files\Intel\Power Gadget 3.6\PowerLog3.0.exe\""

import argparse
import subprocess
from datetime import datetime


logfile = f"\"power-logs\\PowerLog-{str(datetime.now()).replace(':','-')}\""
parser = argparse.ArgumentParser(description="cmd line tool for measuring energy consumption while executing a program and extracting main results")
parser.add_argument('-o', '--output', dest='outfile', default=logfile)
parser.add_argument('-ctype', dest="cmdtype", default='python3')
parser.add_argument('-r', '--resolution', dest='resolution', default=5)
parser.add_argument('-v', '--verbose', dest='verbose', default=False)
parser.add_argument('-cmd', dest="infile")

args = parser.parse_args()

comm_types={"clang":f"{args.infile}", "python3":f"python {args.infile}"}
data = args.outfile

proc = f"{power_path} -resolution {args.resolution} -file {args.outfile} -cmd {comm_types[args.cmdtype]}"
print("Running command:\n",proc)

completed = subprocess.run(proc)
print(completed.stdout)
print("Measurement Completed -- Analyzing")

import polars as pl

df = pl.read_csv(data.replace("\"",""))
print(df)


