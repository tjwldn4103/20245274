import random

def make_matrix(n):
    matrix = []

    for i in range(n):
        row = []

        for j in range(n):
            num = random.randint(1, n * n * 10 - 1)
            row.append(num)

        matrix.append(row)

    return matrix


def print_matrix(matrix):
    for row in matrix:
        for num in row:
            print(f"{num:5}", end="")
        print()


n = int(input("N 입력: "))

A = make_matrix(n)

print("A 행렬")
print_matrix(A)
