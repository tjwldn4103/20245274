n = int(input())

for i in range(2 * n):
    if i % 2 == 0:
        print('* ' * n)
    else:
        print(' ' + '* ' * (n - 1))
