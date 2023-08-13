from math import ceil

n = int(input())
hp = list(map(int, input().split()))
a = [9, 3, 1]
result = 0

if n == 1:
    result = ceil(hp[0]/9)

else:
    while any(num > 0 for num in hp):
        hp = sorted(hp, reverse=True)
        hp = [h - a for h, a in zip(hp, a)]
        result += 1
        if all(num <= 0 for num in hp):
            break
    
print(result)