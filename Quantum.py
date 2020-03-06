import cirq
import numpy as np

nqubits = 5
qubits  = [cirq.GridQubit(0, x) for x in range(nqubits)]

circuit = cirq.Circuit()

# Apply Hadamard operation on every qubit
circuit.append(cirq.H(q) for q in qubits)
# Apply CNOT operation on (0, 1), (1,2), (2,3), (3,4)
circuit.append(cirq.CNOT(qubits[i], qubits[i+1]) for i in range(nqubits-1))
# SWAP (0, 4)
circuit.append(cirq.SWAP(qubits[0], qubits[4]))
# Rotate X with pi/2
circuit.append(cirq.rx(np.pi/2)(q) for q in qubits)

# Plot the circuit
print(circuit)
