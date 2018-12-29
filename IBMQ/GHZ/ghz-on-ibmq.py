from qiskit import execute, IBMQ, QuantumCircuit, QuantumRegister, ClassicalRegister, BasicAer
from qiskit.tools.visualization import plot_histogram

# IBMQ.load_accounts()
# print(IBMQ.backends())

circuits = []

# YYX
q_yyx = QuantumRegister(3)
c_yyx = ClassicalRegister(3)
qc_yyx = QuantumCircuit(q_yyx, c_yyx)
qc_yyx.h(q_yyx[0])
qc_yyx.cx(q_yyx[0], q_yyx[1])
qc_yyx.cx(q_yyx[0], q_yyx[2])
qc_yyx.s(q_yyx[0])  # measure_y = s + h + measure_z
qc_yyx.h(q_yyx[0])
qc_yyx.s(q_yyx[1])  # measure_y = s + h + measure_z
qc_yyx.h(q_yyx[1])
qc_yyx.h(q_yyx[2])  # measure_x = h + measure_z
qc_yyx.measure(q_yyx, c_yyx)
circuits.append(qc_yyx)

# YXY
q_yxy = QuantumRegister(3)
c_yxy = ClassicalRegister(3)
qc_yxy = QuantumCircuit(q_yxy, c_yxy)
qc_yxy.h(q_yxy[0])
qc_yxy.cx(q_yxy[0], q_yxy[1])
qc_yxy.cx(q_yxy[0], q_yxy[2])
qc_yxy.s(q_yxy[0])  # measure_y = s + h + measure_z
qc_yxy.h(q_yxy[0])
qc_yxy.h(q_yxy[1])  # measure_x = h + measure_z
qc_yxy.s(q_yxy[2])  # measure_y = s + h + measure_z
qc_yxy.h(q_yxy[2])
qc_yxy.measure(q_yxy, c_yxy)
circuits.append(qc_yxy)

# XYY
q_xyy = QuantumRegister(3)
c_xyy = ClassicalRegister(3)
qc_xyy = QuantumCircuit(q_xyy, c_xyy)
qc_xyy.h(q_xyy[0])
qc_xyy.cx(q_xyy[0], q_xyy[1])
qc_xyy.cx(q_xyy[0], q_xyy[2])
qc_xyy.h(q_xyy[0])  # measure_x = h + measure_z
qc_xyy.s(q_xyy[1])  # measure_y = s + h + measure_z
qc_xyy.h(q_xyy[1])
qc_xyy.s(q_xyy[2])  # measure_y = s + h + measure_z
qc_xyy.h(q_xyy[2])
qc_xyy.measure(q_xyy, c_xyy)
circuits.append(qc_xyy)

# XXX
q_xxx = QuantumRegister(3)
c_xxx = ClassicalRegister(3)
qc_xxx = QuantumCircuit(q_xxx, c_xxx)
qc_xxx.h(q_xxx[0])
qc_xxx.cx(q_xxx[0], q_xxx[1])
qc_xxx.cx(q_xxx[0], q_xxx[2])
qc_xxx.h(q_xxx[0])  # measure_x = h + measure_z
qc_xxx.h(q_xxx[1])  # measure_x = h + measure_z
qc_xxx.h(q_xxx[2])  # measure_x = h + measure_z
qc_xxx.measure(q_xxx, c_xxx)
circuits.append(qc_xxx)

n = 8192
backend = BasicAer.get_backend('qasm_simulator')
#backend = IBMQ.get_backend('ibmq_qasm_simulator')
#backend = IBMQ.get_backend('ibmqx4')
job_sim = execute(circuits, backend, shots=n)
sim_result = job_sim.result()


counts_yyx = sim_result.get_counts(qc_yyx)
counts_xxx = sim_result.get_counts(qc_xxx)
counts_yxy = sim_result.get_counts(qc_yxy)
counts_xyy = sim_result.get_counts(qc_xyy)


prob_yyx = {k: v / n for k, v in counts_yyx.items()}
prob_xxx = {k: v / n for k, v in counts_xxx.items()}
prob_yxy = {k: v / n for k, v in counts_yxy.items()}
prob_xyy = {k: v / n for k, v in counts_xyy.items()}

legend = ['YYX', 'XXX', 'YXY', 'XYY']
plot_histogram([counts_yyx, counts_xxx, counts_yxy, counts_xyy],
               figsize=(20, 10), legend=legend, title='GHZ experiment', bar_labels=False).savefig("out.png")


# print(prob)
# plot_histogram(counts).savefig("out_xyy.png")
