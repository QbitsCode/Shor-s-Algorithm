from sympy import N
from RSA import CreateKeys, GeneratePrivateFromPublic, PreSetPrimes

from qiskit.algorithms import Shor
from qiskit.utils import QuantumInstance
import numpy as np
from qiskit import QuantumCircuit, Aer, execute, IBMQ
from qiskit.tools.visualization import plot_histogram

msg = 9
#public, private = CreateKeys.execute(1,15)
public, private = PreSetPrimes.execute(3, 7)
#public, private = PreSetPrimes.execute(61, 97)
print(private.d)


c = public.encrypt(msg)
print(c)

backend = Aer.get_backend('qasm_simulator')
quantum_instance = QuantumInstance(backend, shots=1000)
#my_shor = Shor(N=keys.n, a=2, quantum_instance=quantum_instance)
my_shor = Shor(quantum_instance=quantum_instance)
""" IBMQ.load_account()
provider = IBMQ.get_provider('ibm-q')
qcomp = provider.get_backend('ibmq_bogota')
my_shor = Shor(quantum_instance=qcomp) """

result = my_shor.factor(N=public.n, a=2)
print(result)
factors = result._factors[0]
print(factors)

gPrivate = GeneratePrivateFromPublic.execute(factors[0], factors[1], public)
print(gPrivate.d)
m = gPrivate.decrypt(c)
print(m)