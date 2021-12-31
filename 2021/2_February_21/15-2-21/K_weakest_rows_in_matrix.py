matrix = [[1, 1, 0, 0, 0],
          [1, 1, 1, 1, 0],
          [1, 0, 0, 0, 0],
          [1, 1, 0, 0, 0],
          [1, 1, 1, 1, 1]]


def KWeakestRows(matrix, k):
    sums = list()
    for i, row in enumerate(matrix):
        sums.append((sum(row), i))
    sums.sort()
    return [x[1] for x in sums[:k]]


print(KWeakestRows(matrix, 3))
