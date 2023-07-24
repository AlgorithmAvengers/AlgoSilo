import sys
input = sys.stdin.readline

n = int(input())
ahri = list(input().strip().split())
dasol = []
for _ in range(n):
    dasol.append(list(input().strip().split()))

# 판짜기
# 보는 방향 1: down 2: L 3: up 4: R
dx = [0, 1, 0, -1]
dy = [1, 0, -1, 0]
x, y = 1, 1
ori = 0

# 좀비 및 전등 색출
zombie = []
light = []
dict_key = []
for i in range(n):
    for j in range(n):
        dict_key.append((j+1,i+1))
        if dasol[i][j] == 'Z':
            zombie.append((j+1,i+1,0))
        if dasol[i][j] == 'S':
            light.append((j+1,i+1))
phew_zone = {key: False for key in dict_key}

# game start
for i in range(len(ahri)):
    for s in range(len(light)):
        sx, sy = light[s]
        if x == sx and y == sy:
            for a in [x-1, x, x+1]:
                for b in [y-1, y, y+1]:
                    try:
                        phew_zone[(a,b)] = True
                    except:
                        pass
    
    if ahri[i] == 'F':
        new_x = x + dx[ori]
        new_y = y + dy[ori]
    if ahri[i] == 'L':
        ori = ori + 1
    if ahri[i] == 'R':
        ori = ori - 1

    if new_x < 1 or new_y < 1 or new_x > n or new_y > n:
        if dasol[new_y-1][new_x-1] == 'Z':
            if phew_zone[(new_x, new_y)] == True:
                pass
            else:
                print("Aaaaaah!")
                break
        for z in range(len(zombie)):
            zx, zy, z_ori = zombie[z]
            new_zx = zx + dx[z_ori]
            new_zy = zy + dy[z_ori]
            if new_zx < 1 or new_zy < 1 or new_zx > n or new_zy > n:
                zombie[z] = (zx, zy, z_ori+2)
            else:
                zombie[z] = (new_zx, new_zy, z_ori)
                dasol[zy-1][zx-1] = '0'
                dasol[new_zy-1][new_zx-1] = 'Z'
        continue
  
    if dasol[new_y-1][new_x-1] == 'Z':
        if phew_zone[(new_x, new_y)] == True:
            pass
        else:
            print("Aaaaaah!")
            exit()

    for z in range(len(zombie)):
        zx, zy, z_ori = zombie[z]
        new_zx = zx + dx[z_ori]
        new_zy = zy + dy[z_ori]
        if new_zx < 1 or new_zy < 1 or new_zx > n or new_zy > n:
            zombie[z] = (zx, zy, z_ori+2)
        else:
            zombie[z] = (new_zx, new_zy, z_ori)
            dasol[zy-1][zx-1] = '0'
            dasol[new_zy-1][new_zx-1] = 'Z'
        
    x, y = new_x, new_y
    
print("Phew...")