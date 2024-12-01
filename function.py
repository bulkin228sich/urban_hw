def get_matrix( n, m, value):
    if value < 1:
        return []
    matrix = []
    for i in range(n):
        x = []
        for j in range(m):
            x.append(value)
        matrix.append(x)

    return matrix

x = get_matrix(3,4, 10)
print(x)