from collections import deque

def manhattan_distance(x, y, nx, ny):
    return abs(nx - x) + abs(ny - y)


def bfs():
    # 편의점에 들리지 않아도 바로 갈 수 있다면 빠르게 True로 판단할 수 있도록 함
    if manhattan_distance(home_x, home_y, rock_x, rock_y) <= 1000:
        can_go[n] = True
        return

    que = deque()

    # home에서 갈 수 있는 convenience store 찾아서 que에 저장
    for i in range(len(store)):
        dist = manhattan_distance(home_x, home_y, store[i][0], store[i][1])
        if dist <= 1000:
            que.append(store[i])
            can_go[i] = True

    # 갈 수 있는 편의점을 기준으로 연결되어 갈 수 있는 편의점이 있는지 확인
    while que:
        cx, cy = que.popleft()
        for i in range(len(store)):
            dist = manhattan_distance(cx, cy, store[i][0], store[i][1])
            if dist <= 1000 and not can_go[i]:
                que.append(store[i])
                can_go[i] = True

t = int(input())

for _ in range(t):
    n = int(input())
    # rock festival의 위치를 append하므로 n+1만큼의 길이가 필요함
    can_go = [False] * (n + 1)
    store = []

    home_x, home_y = map(int, input().split())

    for _ in range(n):
        store.append([int(a) for a in input().split()])

    rock_x, rock_y = map(int, input().split())
    store.append([rock_x, rock_y])

    bfs()

    if can_go[n] == True:
        print('happy')
    else:
        print('sad')