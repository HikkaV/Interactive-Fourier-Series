import argparse
import numpy as np
parser = argparse.ArgumentParser()


def parse_args():
    parser.add_argument('--func', help='Name of function to be fit to', default='power_func', type=str)
    parser.add_argument('--n', help='Number of Fourier series members', default=5, type=int)
    parser.add_argument('--k', help='The power for power function', default=2, type=int)
    parser.add_argument('--s', help='True if to save the resulting gif', default=False, type=bool)
    parser.add_argument('--high', help='High limit for function', default=np.pi, type=np.float)
    parser.add_argument('--low', help='Low limit for function', default=-np.pi, type=np.float)
    args = parser.parse_args()
    return args
