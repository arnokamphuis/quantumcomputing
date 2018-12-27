from qiskit import execute, IBMQ, QuantumCircuit, QuantumRegister, ClassicalRegister, BasicAer

try:
    IBMQ.load_accounts()
except:
    print("""WARNING: There's no connection with the API for remote backends.
             Have you initialized a file with your personal token?
             For now, there's only access to local simulator backends...""")

# see a list of available remote backends
# print("\n(IBMQ Backends)")
# print(IBMQ.backends())

q = QuantumRegister(2)
c = ClassicalRegister(2)
qc = QuantumCircuit(q, c)

qc.h(q[0])
qc.cx(q[0], q[1])
qc.measure(q, c)

# backend = BasicAer.get_backend('qasm_simulator')
backend = IBMQ.get_backend('ibmq_qasm_simulator')
job_sim = execute(qc, backend)
sim_result = job_sim.result()

print(sim_result.get_counts(qc))
