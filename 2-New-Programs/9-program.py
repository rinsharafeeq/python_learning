
#Task: Given a matrix as a list of lists (all rows same length), write transpose(matrix)
# that returns a new matrix with rows and columns swapped.
#Transpose a matrix (list of lists)
def transpose(matrix):
    rows = len(matrix)
    cols = len(matrix[0]) if rows > 0 else 0
    transposed = []
    for c in range(cols):
        new_row = []
        for r in range(rows):
            new_row.append(matrix[r][c])
        transposed.append(new_row)
    return transposed
mat = [
    [1, 2, 3],
    [4, 5, 6]
]
print(transpose(mat))