lijst_2D = [
    [11, 12, 34, 14],
    [32, 22, 23, 24],
    [31, 32, 33, 12] 
]

def max_vinder(matrix):
    max_value = float('-inf')  # Start with negative infinity
    max_position = None

    for i, row in enumerate(matrix):
        for j, value in enumerate(row):
            if value > max_value:
                max_value = value
                max_position = (i, j)
    
    return max_value, max_position

max_val, (row, col) = max_vinder(lijst_2D)
print(f"The maximum value is {max_val} at position (row: {row}, column: {col})")