# Start from the official MiniZinc image (includes Gecode, Chuffed, OR-Tools)
FROM minizinc/minizinc:2.8.3

# Install Python 3 and pip
RUN apt-get update && apt-get install -y python3 python3-pip && rm -rf /var/lib/apt/lists/*

# Install Python packages: PuLP and Z3
RUN pip3 install pulp z3-solver

# Set the working directory inside the container
WORKDIR /app

# Copy your whole project into the container
COPY . .

# By default, open a bash terminal
ENTRYPOINT ["/bin/bash"]
