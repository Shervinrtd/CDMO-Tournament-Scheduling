
import os
import subprocess

# Larger team sizes for testing
team_sizes = [12, 14, 16]

# Each tuple is (name, path to script, result folder)
solvers = [
    ("CP", "source/CP/cp_runner.py", "res/CP"),
    ("SAT", "source/SAT/sat_solver.py", "res/SAT"),
    ("SMT", "source/SMT/smt_solver.py", "res/SMT"),
    ("MIP", "source/MIP/mip_solver.py", "res/MIP"),
]

for n in team_sizes:
    print(f"=== Running for n = {n} teams ===")
    for name, script, out_dir in solvers:
        print(f"--> {name} solver")
        os.makedirs(out_dir, exist_ok=True)
        try:
            subprocess.run(["python3", script, str(n)], check=True)
        except subprocess.CalledProcessError:
            print(f"[!] Error occurred while running {name} for n = {n}")
    print()
