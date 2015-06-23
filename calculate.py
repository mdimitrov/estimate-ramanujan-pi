from multiprocessing import Pool
from time import time
from datetime import datetime
from functools import reduce
from argparser import parser
from os import getpid
import decimal


D = decimal.Decimal
C = decimal.getcontext()

C.prec = 1000


def multiply(x, y): return C.multiply(x, y)


def divide(x, y): return C.divide(x, y)


def addition(x, y): return C.add(x, y)


def power(x, y): return C.power(x, y)


def sqrt(x): return C.sqrt(x)


def log(message, loud=False):
    if args.quiet is not True or loud:
        print(message)


def factorial(n):
    result = 1
    while n > 1:
        result *= n
        n = n - 1
    return D(result)


def get_ramanujan_term(k):
    pid = getpid()
    log('...({}) is calculating term for k={}'.format(pid, k))
    k = D(k)
    num = multiply(factorial(4 * k), addition(D(1103), multiply(D(26390), D(k))))
    den = multiply(power(factorial(k), D(4)), power(D(396), multiply(D(4), D(k))))
    term = divide(num, den)
    log('...({}) is done for k={}'.format(pid, k))
    return term

if __name__ == '__main__':
    args = parser.parse_args()

    if args.precision is 0:
        print('default precision 0 will be used')

    # start worker processes
    ts = time()
    log('Started at {}'.format(datetime.now()), True)

    with Pool(processes=args.tasks) as pool:
        factor = divide(multiply(D(2), sqrt(D(2))), D(9801))
        all_terms = pool.map(get_ramanujan_term, range(args.precision))
        the_sum = reduce(lambda x, y: addition(x, y), all_terms)

        with open(args.output_file, 'w') as f:
            f.write('Pi({}) = {}'.format(args.precision, 1 / multiply(factor, the_sum)))

    log('Finished at {}'.format(datetime.now()), True)
    log('Took {}'.format(time() - ts), True)
