import cupy as cp
import time

vetor =  cp.random.randint(0, 99, 100000000)
print(vetor)
b= time.time()
soma= vetor.sum()
a= time.time()

print(f"tempo de execução: {a - b}")
print(soma)