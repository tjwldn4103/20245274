import random

def make_matrix(n):
    matrix = []

    for i in range(n):
        row = []

        for j in range(n):
            num = random.randint(1, n*n*10-1)
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

print("원래 행렬")
print_matrix(A)


T = []

for i in range(n):

    row = []

    for j in range(n):

        row.append(A[j][i])

    T.append(row)

print("전치행렬")
print_matrix(T)
