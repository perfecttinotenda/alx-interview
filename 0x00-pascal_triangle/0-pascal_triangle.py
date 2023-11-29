def pascal_triangle(n):
    """
        This will
        Generate the  Pascals' triangle 
        up_to_the nth row.
    """
    triangle = []

    if n <= 0:
        return triangle

    for i in range(n):
        row = [1]  # First element of the triangle is always 1
        if triangle:
            last_row = triangle[-1]
            # This will Calculate the next row_based on prevz row
            row.extend([sum(pair) for pair in zip(last_row, last_row[1:])])
            row.append(1)  # The Last element of Pascals' triangle is always 1
        triangle.append(row)

    return triangle

if __name__ == "__main__":
    n = 5
    result = pascal_triangle(n)
    for row in result:
        print(row)
