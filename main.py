from sympy import N
from RSA import CreateKeys, GeneratePrivateFromPublic, PreSetPrimes

from qiskit.algorithms import Shor
from qiskit.utils import QuantumInstance
import numpy as np
from qiskit import QuantumCircuit, QuantumRegister, Aer, execute, IBMQ
from qiskit.tools.visualization import plot_histogram

msg = 9
#public, private = CreateKeys.execute(1,15)
public, private = PreSetPrimes.execute(5, 23)
#public, private = PreSetPrimes.execute(61, 97)
print("original d: ",private.d)


c = public.encrypt(msg)
print("ciphertext: ",c)
print("n: ",public.n)
print("bit length: ",public.n.bit_length())
n = public.n.bit_length()

up_qreg = QuantumRegister(2 * n, name="up")
down_qreg = QuantumRegister(n, name="down")
aux_qreg = QuantumRegister(n + 2, name="aux")
circuit = QuantumCircuit(up_qreg, down_qreg, aux_qreg, name=f"Shor()")
print("qbits: ",len(circuit.qubits))

""" backend = Aer.get_backend('qasm_simulator')
quantum_instance = QuantumInstance(backend, shots=1000)
#my_shor = Shor(N=keys.n, a=2, quantum_instance=quantum_instance)
my_shor = Shor(quantum_instance=quantum_instance) """

IBMQ.load_account()
provider = IBMQ.get_provider('ibm-q')
qcomp = provider.get_backend('simulator_mps')
my_shor = Shor(quantum_instance=qcomp)

result = my_shor.factor(N=public.n, a=2)
#print(result)
factors = result._factors[0]
print("factors: ",factors)

gPrivate = GeneratePrivateFromPublic.execute(factors[0], factors[1], public)
print("generated d: ",gPrivate.d)
m = gPrivate.decrypt(c)
print("message: ",m)