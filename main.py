from RSA.usecase.createKeys import CreateKeys
from RSA.usecase.generateKeysFromPublic import GenerateKeysFromPublic

from qiskit.aqua.algorithms import Shor
from qiskit.aqua import QuantumInstance
import numpy as np
from qiskit import QuantumCircuit, Aer, execute
from qiskit.tools.visualization import plot_histogram

msg = 9
keys = CreateKeys.execute(1,30)
print(keys.d)


c = keys.encrypt(msg)
print(c)

backend = Aer.get_backend('qasm_simulator')
quantum_instance = QuantumInstance(backend, shots=1000)
my_shor = Shor(N=keys.n, a=2, quantum_instance=quantum_instance)

result = Shor.run(my_shor)
factors = result.get("factors")[0]
print(factors)

gkeys = GenerateKeysFromPublic.execute(factors[0], factors[1], keys.e, keys.n)
print(gkeys.d)
m = gkeys.decrypt(c)
print(m)