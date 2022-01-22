from RSA.usecase.createKeys import CreateKeys
from RSA.usecase.generateKeysFromPublic import GenerateKeysFromPublic

from qiskit.aqua.algorithms import Shor
from qiskit.aqua import QuantumInstance
import numpy as np
from qiskit import QuantumCircuit, Aer, execute
from qiskit.tools.visualization import plot_histogram

msg = 9
keys = CreateKeys.execute(1,30)
c = keys.encrypt(msg)

backend = Aer.get_backend('qasm_simulator')
quantum_instance = QuantumInstance(backend, shots=1000)
my_shor = Shor(N=keys.n, a=2, quantum_instance=quantum_instance)

Shor.run(my_shor)
l = my_shor._get_factors()
gkeys = GenerateKeysFromPublic.execute(l[0], l[1], keys.e, keys.n)

m = gkeys.decrypt(c)