from qiskit import QuantumCircuit
from qiskit_aer import AerSimulator

#a circuit with 1 qubit and 1 classical bit
circuit = QuantumCircuit(1, 1)

#the qubit in Superposition
circuit.h(0)

#Measure the qubit and store the result in the classical bit
circuit.measure(0, 0)

#AerSimulator runs the experiment 1000 times
simulator = AerSimulator()
result = simulator.run(circuit, shots=100000).result()

#counts
counts = result.get_counts()
print(f"Quantum Experiment Results: {counts}")