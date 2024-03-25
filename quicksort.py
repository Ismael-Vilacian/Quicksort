import random
import matplotlib.pyplot as plt
import time
import psutil  

def particiona(A, p, r):
    x = A[r]
    i = p - 1

    for j in range(p, r):
        if A[j] <= x:
            i += 1
            A[i], A[j] = A[j], A[i]

    A[i + 1], A[r] = A[r], A[i + 1]
    return i + 1

def quicksort(A, p, r, memory_usage, time_elapsed):
    if p < r:
        q = particiona(A, p, r)
        quicksort(A, p, q - 1, memory_usage, time_elapsed)
        quicksort(A, q + 1, r, memory_usage, time_elapsed)

        mem_usage = psutil.virtual_memory().used / 1024 / 1024 
        memory_usage.append(mem_usage)
        time_elapsed.append(time.time() - start_time)


memory_usage = []
time_elapsed = []

A = [random.randint(1, 100000) for _ in range(1000)]

start_time = time.time()
quicksort(A, 0, len(A) - 1, memory_usage, time_elapsed)

print("Lista Ordenada:", A)


plt.figure(figsize=(10, 5))
plt.subplot(1, 2, 1)
plt.plot(time_elapsed)
plt.xlabel('Iterações')
plt.ylabel('Tempo decorrido (s)')
plt.title('Tempo de Ordenação')

plt.subplot(1, 2, 2)
plt.plot(memory_usage)
plt.xlabel('Iterações')
plt.ylabel('Uso de Memória (MB)')
plt.title('Uso de Memória')

plt.tight_layout()
plt.show()