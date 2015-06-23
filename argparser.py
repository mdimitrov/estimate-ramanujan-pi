import argparse

parser = argparse.ArgumentParser()
parser.add_argument('-p', type=int, default=1, dest='precision', help='a number of terms; default: 1')
parser.add_argument('-t', type=int, default=None, dest='tasks', help='a number of processes; default: number of cores')
parser.add_argument('-o', default='output.txt', dest='output_file', help='specify output file; default: output.txt')
parser.add_argument('-q', action='store_true', dest='quiet', help='quite mode')
