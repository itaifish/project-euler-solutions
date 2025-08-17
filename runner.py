import sys
import os
from pathlib import Path
import subprocess
import statistics

FILES_DIR = Path("/euler-solutions")

if len(sys.argv) != 2:
    print(f"Usage: {sys.argv[0]} <num_runs>")
    exit(-1)

num_runs = int(sys.argv[1])

# mapping from filename -> [runtimes]
runtimes = {}

print(f"Running input files {num_runs} times to collect statistics")
for file in os.listdir(FILES_DIR):
    file_path = FILES_DIR / Path(file)

    if file_path.suffix != ".py":
        print(f"Expected all files to have extension .py, but got {file_path}")
        exit(-2)

    for _ in range(0, num_runs):
        result = subprocess.run(["python", file_path], capture_output=True, check=True)

        last_line = result.stdout.strip().split(b"\n")[-1]
        last_line_int = float(last_line)

        runtimes.setdefault(file, []).append(last_line_int * 1_000) # convert to milliseconds

runtime_statistics = {
    filename: (min(runtimes), statistics.median(runtimes), max(runtimes))
    for filename, runtimes in runtimes.items()
}

print("Individual Runtime Statistics (min, median, max) in milliseconds")
for filename, filename_statistics in sorted(list(runtime_statistics.items())):
    print(f"{filename}: {filename_statistics}")

overall_runtime_statistics = tuple(sum(runtimes) for runtimes in zip(*runtime_statistics.values()))
print("Overall Runtime Statistics (min, median, max) in milliseconds")
print(overall_runtime_statistics)