import threading, random, time
import decimal, math, functools
from queue import Queue
import sys

D = decimal.Decimal
C = decimal.getcontext()

C.prec = 1000


def multiply(x, y): return C.multiply(x, y)


def divide(x, y): return C.divide(x, y)


def addition(x, y): return C.add(x, y)


def power(x, y): return C.power(x, y)


def sqrt(x): return C.sqrt(x)


def factorial(n):
    result = 1
    while n > 1:
        result *= n
        n = n - 1
    return D(result)


def get_ramanujan_term(k):
    num = multiply(factorial(4 * k), addition(D(1103), multiply(D(26390), D(k))))
    den = multiply(power(factorial(k), D(4)), power(D(396), multiply(D(4), D(k))))
    term = divide(multiply(factor, num), den)
    return term


def worker(num):
    global total
    while True:
        item = q.get()
        if item is None:
            break
        print('...({}) working'.format(item))
        term = get_ramanujan_term(item)
        with lock:
            total = addition(global_total, term)
        print('...({}) done'.format(item))
        q.task_done()


def with_threads(num_terms, num_threads):
    ts = time.time()
    threads = []
    for i in range(num_threads):
        t = threading.Thread(target=worker, args=(i,))
        t.start()
        threads.append(t)

    for item in range(num_terms):
        q.put(item)

    # block until all tasks are done
    q.join()

    # stop workers
    for i in range(num_threads):
        q.put(None)
    for t in threads:
        t.join()

    print(1 / global_total)
    print('Took {}'.format(time.time() - ts))


def no_threads(top):
    k = D(0)
    ts = time.time()
    total = D(0)
    while True:
        total = addition(total, get_ramanujan_term(k))
        print(k)
        if k >= top:
            break
        k += 1
    print(1/total)
    print('Took {}'.format(time.time() - ts))

factor = divide(multiply(D(2), sqrt(D(2))), D(9801))
global_total = D(0)
lock = threading.Lock()
q = Queue()
if __name__ == '__main__':
    precision = 2048
    num_threads = 8
    no_threads(precision)
    # with_threads(precision, num_threads)
