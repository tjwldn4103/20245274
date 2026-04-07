arr = []

for _ in range(9):
    arr.append(int(input()))

max_val = max(arr)
index = arr.index(max_val) + 1

print(max_val)
print(index)
