def manhattan_distance(x, y, nx, ny):
    return abs(nx-x) + abs(ny-y)

t = int(input())
can_go = [True] * (t+1)

for i in range(t):
    n = int(input())
    home_x, home_y = map(int, input().split())

    if n == 0:
        rock_x, rock_y = map(int, input().split())
        dist = manhattan_distance(home_x, home_y, rock_x, rock_y)
        if dist > 1000:
            can_go[i] = False
            continue

    store = []
    for j in range(n):
        store.append([int(a) for a in input().split()])

    rock_x, rock_y = map(int, input().split())
    store.append([rock_x, rock_y])
    
    x = home_x
    y = home_y
    nx = store[0][0]
    ny = store[0][1]
    for k in range(n+1):
        if can_go:
            dist = manhattan_distance(x, y, nx, ny)
            if dist > 1000:
                can_go[i] = False
                break
            else:
                nx = store[k+2][0]
                ny = store[k+2][1]

for _ in range(t):
    if can_go[_] is False:
        print("sad")
    else:
        print("happy")