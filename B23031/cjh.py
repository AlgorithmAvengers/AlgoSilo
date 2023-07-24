n = int(input())
orders = list(input())

# 남 -> 동 -> 북 -> 서 로 움직이는 방향
move = [(0, 1), (1, 0), (-1, 0), (0, -1)]
# switch를 켜야하는 방향
switch_move = [(-1, 0), (0, 1), (1, 0), (0, -1), (-1, -1), (-1, 1), (1, 1), (1, -1)]
# zombie들의 위치 저장
zombies = []
# input으로 주어지는 값 저장
maps = []
# 처음 시작점
x, y = 0, 0
# 처음 시작 방향(move의 list index와 매칭)
d = 0

# input으로 받은 map 저장
for i in range(n):
    a = list(input())
    for j in range(n):
        if a[j] == 'Z': # 좀비체크
            zombies.append((i, j, 2))
    maps.append(a)

# order에 따라 이동하는 방향 정하기
for order in orders:
    if order == 'F':
        dx, dy = move[d]
        nx = x + dx
        ny = y + dy
        if 0 <= nx < n and 0 <= ny < n:
            x, y = nx, ny
    # 'F'를 제외하고는 실제 이동하지 않고 방향 전환만 이루어짐
    elif order == 'L':
        d = (d+1)%4
    else: # order == 'R'
        d = (d+3)%4

    # order에 따라 방향을 이동하면서 중간에 switch가 있는지, 불이 켜져 있는 곳인지 확인
    #'S' -> 스위치가 있는 경우, 's' -> 불이 켜진 곳, 'A' -> 아직 켜지 않은 스위치가 있지만, 불은 켜진 곳
    """
    'S'와 'A'를 분리하여 생각하는 이유는 'S'를 확인하고 모두 근처를 s로 변경할 경우, 
    스위치가 있는 것이 확인되지 않을 수 있으므로 켠 스위치와 켜지 않은 스위치를 구분하는 것
    """
    if maps[x][y] == 'S' or maps[x][y] == 'A':
        maps[x][y] = 's'
        for b in range(8):
            dx, dy = switch_move[b]
            nx = x + dx
            ny = y + dy
            if 0 <= nx < n and 0 <= ny < n:
                if maps[nx][ny] == 'S':
                    maps[nx][ny] = 'A'
                else:
                    maps[nx][ny] = 's'
    
    # zombie와 아리가 같이 이동하면서 어두운 곳에서 만나는지, 밝은 곳에서 만나는지 확인
    """ 좀비는 여러 명일 수 있으므로, 아리가 먼저 움직이기 떄문에 움직였을 때 그 자리에 좀비가 있는지와 
    아리가 움직인 후에 좀비가 같이 움직여서 아리의 자리로 온 경우를 모두 고려해야함)
    """
    for z in range(len(zombies)):
        zx, zy, zd = zombies[z]
        if x == zx and y == zy:
            if maps[x][y] != 's' and maps[x][y] != 'A': # Case 1: 아리가 움직이고 그 자리에 좀비가 있는 경우 체크('A'를 체크하는 이유는 스위치를 먼저 켜게 되기 떄문)
                print('Aaaaaah!')
                exit()
        # 좀비도 아리와 함께 기존의 방향으로 이동하게 됨
        dx, dy = move[zd]
        znx = zx + dx
        zny = zy + dy
        if 0 <= znx < n and 0 <= zny < n:
            zx, zy = znx, zny
            zombies[z] = (zx, zy, zd)
        else: # 벽 부딪치는 경우(좀비는 남북으로만 이동하게 됨)
            if zd == 2:
                zd = 0
            else:
                zd = 2
            zombies[z] = (zx, zy, zd)
        if x == zx and y == zy: # Case 2: 아리가 움직인 이후 좀비도 움직여서 좀비가 아리의 자리에 온 경우
            if maps[x][y] != 's' and maps[x][y] != 'A':
                print('Aaaaaah!')
                exit()
print('Phew...')