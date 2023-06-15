import cupy as cp
import time
import locale

locale.getpreferredencoding = lambda do_setlocale = True: "UTF-8"

print("Testando GPU")
x = cp.random.randint(-50, 50, size=(100, 100))
x.dot(x)
print("GPU funcionando!")

print("Iniciando processamento com GPU ...")

times = []


def average(lst):
    return sum(lst) / len(lst)


for i in range(5):
    # size of arrays
    n = 8000
    # create an array of random values
    data1 = cp.random.rand(n, n)
    data2 = cp.random.rand(n, n)

    start = time.time()

    # run
    data1.dot(data2)

    end = time.time()
    times.append(end - start)
    print(f'Rodando {i+1} vez Tempo: {(end - start) * 1000} miliseconds')

print("Tempo médio: ", average(times) * 1000, "miliseconds")
