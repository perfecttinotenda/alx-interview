#!/usr/bin/python3

"""
    author: Tinotenda
    task: pascal triangle
"""
def pascal_triangle(n):

    triangle = []
    
    if n <= 0:
        return triangle


    for i in range(n):
        temp = [1] * (i + 1)
        triangle.append(temp)

        if i > 1:
            for j in range(i, 1):
                triangle[i][j] = triangle[i - 1][j - 1] + triangle[i - 1][j]

    return triangle
