n = int(input())
arr = list(map(int, input().split()))

arr.sort()

result = 0

for i in range(n):
    result += arr[i] * i - arr[i] * (n - i - 1)

print(result * 2)
