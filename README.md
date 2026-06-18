# Quantum Coin Flipper (Superposition Simulator)

A Qiskit program demonstrating fundamental quantum superposition using a Hadamard (H) gate and the Aer simulator.

## Project Overview
This project uses IBM's Qiskit framework to place a single qubit into a state of perfect quantum superposition. Think of it like spinning a coin in the air—while spinning, it is a blend of both heads and tails. 

The program runs this experiment 100,000 times to show how true quantum randomness works in practice.

---

## How It Works

### 1. Quantum Superposition
A standard computer bit can only ever be a 0 or a 1. A quantum bit (qubit) starts at |0> but can be put into a superposition state using a Hadamard (H) gate. 

When the gate is applied, the qubit has an exactly equal 50% chance of collapsing into a 0 or a 1 the moment it is measured.

### 2. Quantum Circuit Workflow
1. **Initialization**: Creates a circuit with 1 qubit and 1 classical bit.
2. **Superposition**: Applies the H gate to Qubit 0, putting it into a 50/50 state.
3. **Measurement**: Forces the qubit to choose a definitive state (0 or 1) and saves that result into the classical bit.
4. **Simulation**: Executes this entire workflow 100,000 times using AerSimulator.

---

## Prerequisites & Installation

Install the required packages via pip:
```bash
pip install qiskit qiskit-aer
```

---

## How to Run

1. Save the code into a file named `quantum_coin.py`.
2. Execute the script in your terminal:
```bash
python quantum_coin.py
```

---

## Expected Output

The simulator outputs a dictionary containing the frequency of each measured state. Because a Hadamard gate creates a perfect 50/50 split, your total counts for 0 and 1 will be nearly identical.

Expect results close to this distribution out of 100,000 shots:
* **0**: ~50,000 times (50%)
* **1**: ~50,000 times (50%)
