def transpose_matrix(matrix):
    rows = len(matrix)
    cols = len(matrix[0])

    transpose = [[0 for _ in range(rows)] for _ in range(cols)]

    for i in range(rows):
        for j in range(cols):
            transpose[j][i] = matrix[i][j]

    return transpose


matrix = [[98, 88, 78],
           [77, 78, 79],
           [66, 67, 68],
           [32, 33, 31]]

transpose = transpose_matrix(matrix)

print("\nMatriks_Transpose:\n")
for row in transpose:
    print(row)