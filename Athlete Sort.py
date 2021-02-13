#!/bin/python3

import math
import os
import random
import re
import sys



if __name__ == '__main__':
    nm = input().split()

    n = int(nm[0])

    m = int(nm[1])

    arr = []

    for _ in range(n):
        arr.append(list(map(int, input().rstrip().split())))

    k = int(input())
    m = [i[k] for i in arr]
    arr1 = []
    for i in range(len(m)):
        arr1.append(arr[m.index(min(m))])
        m.insert(m.index(min(m)), max(m)+1)
        m.remove(min(m))
    for i in arr1:
        for j in i:
            print(j, end = " ")
        print()
