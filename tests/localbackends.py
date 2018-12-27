from qiskit import BasicAer
for backend in BasicAer.backends():
    print(backend.name())
