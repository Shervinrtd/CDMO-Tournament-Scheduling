# CDMO Sports Tournament Scheduling Project

This project solves the Sports Tournament Scheduling (STS) problem using:
- CP (MiniZinc + Gecode/Chuffed)
- MIP (PuLP + CBC)
- SAT (Z3)
- SMT (Z3)

# Project Overview
This project implements multiple approaches to solve the Sports Tournament Scheduling (STS) problem. The goal is to generate a valid tournament schedule for $n$ teams over a specific number of weeks and periods, satisfying various constraints such as round-robin requirements and home/away balance.The problem is modeled and solved using three distinct methodologies:
* Constraint Programming (CP): Implemented in MiniZinc.
* SAT / SMT: Implemented using the Z3 Theorem Prover in Python.
* Mixed-Integer Linear Programming (MIP): Implemented using PuLP in Python.

---

# Model Details
**Constraints Implemented**
The models generally enforce the following rules (based on the MiniZinc implementation):

1- No Self-Play: A team cannot play against itself.

2- One Match Per Week: Every team plays exactly once per week.

3- Round Robin: Every pair of teams meets exactly once during the tournament.

4- Venue Balance: Teams play at most twice at home (or away) in a given period (consecutive weeks).

5- Symmetry Breaking: Fixed matches for the first week to reduce search space (e.g., Team 1 vs Team 2).

# Objective
* MIP: Specifically minimizes the maximum difference between home and away games for any team.

* CP/SAT/SMT: Primarily focused on finding a feasible solution (satisfiability), though CP supports optimization if configured.
  
## Project Folder Structure

```
CDMO_Proj_STS/
├── check_solution.py
├── Dockerfile
├── README.md
├── run_all.py
├── report/
│   ├── Report.pdf
│   └── Report.tex
├── res/            # This will contain the results
│   ├── CP/
│   ├── MIP/
│   ├── SAT/
│   └── SMT/
└── source/
    ├── CP/
    │   ├── cp_runner.py
    │   └── sts_model.mzn
    ├── MIP/
    │   └── mip_solver.py
    ├── SAT/
    │   └── sat_solver.py
    └── SMT/
        └── smt_solver.py
```

 Make sure the `check_solution.py` script is in the **root project folder**, alongside `res/`.

---

##  Build and Run the Docker Environment

### 1. Open your terminal and go to your project root (where Dockerfile is):
```bash
cd path/to/CDMO_Proj_STS
```

### 2. Build the Docker image:
```bash
docker build -t sts-project .
```

### 3. Run the Docker container:
```bash
docker run -it -v "${PWD}:/app" sts-project
```

This will place you inside `/app` (which is your project root inside the container).

---

## Running the Solvers (Inside Docker)

Run **all solvers for all team sizes (8, 10, 12, 14, 16):**
```bash
python3 run_all.py
```

Or run a **specific solver:**
```bash
python3 source/MIP/mip_solver.py 14
python3 source/SMT/smt_solver.py 12
python3 source/CP/cp_runner.py 14
python3 source/SAT/sat_solver.py 14
```

---

## Results Location

Results are saved in the `res/` folder:
```
res/MIP/{n}.json
res/SMT/{n}.json
res/CP/{n}.json
res/SAT/{n}.json
```

---

##  Checking the Results (Outside Docker)

1. **Exit the Docker container** first:
```bash
exit
```

2. Go to your project folder **(the folder where `check_solution.py` is)**:
```bash
cd path/to/CDMO_Proj_STS
```

3. Run the checker on each results folder:
```bash
python check_solution.py res/MIP
python check_solution.py res/SAT
python check_solution.py res/SMT
python check_solution.py res/CP
```

The checker will show whether the solutions are valid or not.

---

## Notes

- Docker is used to ensure all solvers and dependencies are isolated.
- Solvers apply a 300-second timeout.
- Timeout results will be formatted correctly with an empty solution (`sol=[]`, `time=300`, `optimal=false`, `obj='None'`).
- Symmetry breaking constraints improve model performance.

