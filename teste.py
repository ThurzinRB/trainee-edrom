import numpy


N = int(input())

A = [list(map(float, input().split(' '))) for _ in range(N)]

print(numpy.linalg.det(A))
