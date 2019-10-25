from qiskit import *

qc = QuantumCircuit(2, 2)

for i in range(1):  #A 2 qubit circuit only needs to run once to find the solution 
    qc.h(0)          #put into a superposition of all states
    qc.h(1)

    qc.barrier()

    qc.x(0)

    qc.x(0)          #The classical swap circuit
    qc.cx(0,1)
    qc.x(1)
    qc.cx(1,0)
    qc.x(1)
    qc.cx(0,1)
    qc.x(0)

    qc.barrier()

    qc.cz(0,1)       #inverts the wavefunction for the specified value

    qc.barrier()

                    
    for i in range(2): #The grover diffusion opperator for this given circuit
        qc.x(i)
        qc.h(i)

    qc.barrier()

    qc.x(0)

    qc.x(0)          
    qc.cx(0,1)
    qc.x(1)
    qc.cx(1,0)
    qc.x(1)
    qc.cx(0,1)
    qc.x(0)

    qc.barrier()

    qc.cz(0,1)

    qc.barrier()

    for i in range(2):
        qc.x(i)
        qc.h(i)

qc.measure([0,1], [0,1])

print(qc) #displays the circuit

sim_backend = BasicAer.get_backend('qasm_simulator')
job = execute(qc, sim_backend, shots=1000) #runs 1000 times to get statistics
result = job.result()
print('Qasm simulator : ')
print(result.get_counts(qc))