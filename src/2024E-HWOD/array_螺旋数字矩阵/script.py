def spiral_matrix(n, m):
    # Calculate the minimum number of columns required
    cols = (n + m - 1) // m
    matrix = [['*'] * cols for _ in range(m)]  # Initialize matrix with '*'
    num = 1
    left, right, top, bottom = 0, cols - 1, 0, m - 1

    while num <= n and left <= right and top <= bottom:
        for i in range(left, right + 1):  # Fill top row
            if num <= n:
                matrix[top][i] = str(num)
                num += 1
        top += 1

        for i in range(top, bottom + 1):  # Fill right column
            if num <= n:
                matrix[i][right] = str(num)
                num += 1
        right -= 1

        for i in range(right, left - 1, -1):  # Fill bottom row
            if num <= n:
                matrix[bottom][i] = str(num)
                num += 1
        bottom -= 1

        for i in range(bottom, top - 1, -1):  # Fill left column
            if num <= n:
                matrix[i][left] = str(num)
                num += 1
        left += 1

    return '\n'.join([' '.join(row) for row in matrix])

# Example usage:
# n, m = map(int, input().split())
n, m = 9, 4
print(spiral_matrix(n, m))
