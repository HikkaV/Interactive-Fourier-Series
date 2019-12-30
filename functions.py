import numpy as np


def power_func(x, k=2):
    return np.power(x, k)

def step_func(x):
    y = np.zeros_like(x)
    y[x > 0] = 1
    return y

def natural_log_func(x):
    return np.log(x)


def log2_func(x):
    return np.log2(x)


def log10_func(x):
    return np.log10(x)


def exp_func(x):
    return np.exp(x)


def sigmoid_func(x):
    return 1 / (1 + np.exp(-x))


def relu_func(x):
    return np.maximum(x, 0)

