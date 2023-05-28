# from matrixConvolution import matrix_convolution
# import numpy as np

def transpose(m):
    rows = len(m)
    cols = len(m[0])

    return [[m[c][r] for c in range(cols)] for r in range(rows)]

def dot_product(one, two): return sum([one[i] * two[i] for i in range(len(one))])

def shape(m): return [len(m), len(m[0])]

input_matrix = [
    [1, 1, 1, 1],
    [0, 1, 2, 3],
    [3, 4, 5, 2],
    [1, 0, 0, 1]
]

kernel = [
    [0, 1, 2],
    [2, 3, 1],
    [1, 0, 1]
]

# TODO: winograd transform
