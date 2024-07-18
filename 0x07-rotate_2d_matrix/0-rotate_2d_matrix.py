#!/usr/bin/python3

'''A script to solve matrix in-place to 90 degrees'''


def rotate_2d_matrix(matrix):
    '''Rotates a 2d matrix in-place by 90 degrees'''
    n = len(matrix)

    for i in range(n):
        for j in range(i, n):
            matrix[i][j], matrix[j][i] = matrix[j][i], matrix[i][j]

    for i in range(n):
        matrix[i].reverse()
