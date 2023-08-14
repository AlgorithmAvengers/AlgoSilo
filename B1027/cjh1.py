n = int(input())
buildings = list(map(int, input().split()))

if n == 1:
    print(0)

maxcount = 0
for i in range(n):
    x = i
    y = buildings[i]
    count = 0
    for j in range(n):
        if i == j:
            continue

        nx = j
        ny = buildings[j]

        temp = 0
        for k in range(j-i-1):
            heights = y + (ny-y)*(k+1)/(j-i)
            temp += 1
            if heights >= ny:
                break
        
        if temp == j-i-1:
            count += 1
            
    if maxcount < count:
        maxcount = count

print(maxcount)