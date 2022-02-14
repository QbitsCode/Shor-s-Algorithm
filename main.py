from sympy import N
from RSA import CreateKeys, GenerateKeysFromPublic, PreSetPrimes

from qiskit.algorithms import Shor
from qiskit.utils import QuantumInstance
import numpy as np
from qiskit import QuantumCircuit, Aer, execute
from qiskit.tools.visualization import plot_histogram

msg = 9
#keys = CreateKeys.execute(1,15)
keys = PreSetPrimes.execute(3, 7)
#keys = PreSetPrimes.execute(3, 11)
print(keys.d)


c = keys.encrypt(msg)
print(c)

backend = Aer.get_backend('qasm_simulator')
quantum_instance = QuantumInstance(backend, shots=1000)
#my_shor = Shor(N=keys.n, a=2, quantum_instance=quantum_instance)
my_shor = Shor(quantum_instance=quantum_instance)

result = my_shor.factor(N=keys.n, a=2)
print(result)
factors = result._factors[0]
print(factors)

gkeys = GenerateKeysFromPublic.execute(factors[0], factors[1], keys.e, keys.n)
print(gkeys.d)
m = gkeys.decrypt(c)
print(m)