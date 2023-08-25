import sys
from collections import deque
input = sys.stdin.readline

def bfs(subin: int, sibling: int):
    queue = deque()
    queue.append(subin)
    # memory issue
    visited = dict()
    visited[subin] = 0
    while queue:
        this_turn = queue.popleft()
        new_subin1 = 2 * this_turn
        new_subin2 = this_turn + 1
        new_subin3 = this_turn - 1
        if new_subin1 not in visited:
            queue.append(new_subin1)
            visited[new_subin1] = visited[this_turn] + 1
            if new_subin1 == sibling:
                return visited[new_subin1]
        if new_subin2 not in visited:
            queue.append(new_subin2)
            visited[new_subin2] = visited[this_turn] + 1
            if new_subin2 == sibling:
                return visited[new_subin2]
        if new_subin3 not in visited:
            queue.append(new_subin3)
            visited[new_subin3] = visited[this_turn] + 1
            if new_subin3 == sibling:
                return visited[new_subin3]

x, y = map(int, input().split())

print(bfs(x,y))

# visited[new_subin1]