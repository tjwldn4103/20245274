n = int(input())

num = n
count = 0

while True:
    a = num // 10       # 십의 자리
    b = num % 10        # 일의 자리
    c = (a + b) % 10    # 합의 일의 자리

    num = b * 10 + c    # 새로운 수
    count += 1

    if num == n:
        break

print(count)
