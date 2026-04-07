t = int(input())

for _ in range(t):
    s = input()
    
    score = 0
    total = 0
    
    for c in s:
        if c == 'O':
            score += 1
            total += score
        else:
            score = 0
    
    print(total)
