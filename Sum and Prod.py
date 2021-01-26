import numpy
n, m = map(int, input().split())
a = numpy.array([input().split() for _ in range(n)], int)
sum = numpy.sum(a, axis = 0)
print(numpy.prod(sum))
