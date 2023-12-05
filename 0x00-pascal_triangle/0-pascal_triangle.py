#!/usr/bin/python3

"""
    author: Tinotenda
    task: pascal triangle
"""
def pascal_triangle(n):

    tem = []

    if n <= 0:
        return tem

    for i in range(n):
        roh = [1] * (i + 1)
        tem.append(roh)

        if i > 1:
            for g in range(1, i):
                tem[i][g] = tem[i - 1][g - 1] + tem[i - 1][g]
    return tem