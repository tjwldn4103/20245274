n, k = map(int, input().split())

max_val = 0

for i in range(1, k + 1):
    num = n * i
    rev = int(str(num)[::-1])  # 뒤집기

    if rev > max_val:
        max_val = rev

print(max_val)
