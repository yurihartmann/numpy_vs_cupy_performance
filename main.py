import os
import time
from numpy.random import rand

print(f"Iniciando processamento com {os.getenv('OMP_NUM_THREADS')} Thread(s) ...")

times = []


def average(lst):
    return sum(lst) / len(lst)


for i in range(5):
    # size of arrays
    n = 8000
    # create an array of random values
    data1 = rand(n, n)
    data2 = rand(n, n)

    start = time.time()

    # run
    data1.dot(data2)

    end = time.time()
    times.append(end - start)
    print(f'Rodando {i + 1} vez Tempo: {(end - start) * 1000} miliseconds')

print("Tempo médio: ", average(times) * 1000, "miliseconds")
