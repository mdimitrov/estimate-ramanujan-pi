from multiprocessing import Process, Value, Lock, Pool
from time import sleep, time
import os
from functools import reduce
import decimal


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
    k = D(k)
    # print('... ({}) is calculating for n={}'.format(os.getpid(), k))
    factor = divide(multiply(D(2), sqrt(D(2))), D(9801))
    num = multiply(factorial(4 * k), addition(D(1103), multiply(D(26390), D(k))))
    den = multiply(power(factorial(k), D(4)), power(D(396), multiply(D(4), D(k))))
    term = divide(multiply(factor, num), den)
    return term

if __name__ == '__main__':
    # start worker processes
    ts = time()
    with Pool(processes=8) as pool:
        print(1 / reduce(lambda x, y: addition(x, y), pool.map(get_ramanujan_term, range(2048))))

    print('Took {}'.format(time() - ts))
