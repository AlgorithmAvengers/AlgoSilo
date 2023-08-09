# 메모리 초과
import sys
from collections import deque

input = sys.stdin.readline


def bfs3(enemy: tuple):
    queue = deque()
    queue.append(enemy)
    count = 0
    while queue:
        hp = queue.popleft()
        a, b, c = hp[0] - 9, hp[0] - 3, hp[0] - 1
        d, e, f = hp[1] - 9, hp[1] - 3, hp[1] - 1
        g, h, i = hp[2] - 9, hp[2] - 3, hp[2] - 1
        count += 1
        if a<=0 and e<=0 and i<=0:
            return count
        if a<=0 and e<=0 and i<=0:
            return count
        if b<=0 and d<=0 and i<=0:
            return count
        if b<=0 and f<=0 and g<=0:
            return count
        if c<=0 and d<=0 and h<=0:
            return count
        if c<=0 and e<=0 and g<=0:
            return count
        queue.append((a,e,i))
        queue.append((a,f,h))
        queue.append((b,d,i))
        queue.append((b,f,g))
        queue.append((c,d,h))
        queue.append((c,e,g))


def bfs2(enemy: tuple):
    queue = deque()
    queue.append(enemy)
    count = 0
    while queue:
        hp = queue.popleft()
        a, b = hp[0] - 9, hp[0] - 3
        c, d = hp[1] - 9, hp[1] -3
        count += 1
        if a <= 0 and d<=0:
            return count
        if b <= 0 and c<=0:
            return count
        queue.append((a,d))
        queue.append((b,c))

n = int(input())
if n == 1:
    answer = int(input())//9 + 1
else:
    scv = tuple(map(int, input().split()))

if n == 3:
    answer = bfs3(scv)
if n == 2:
    answer = bfs2(scv)

print(answer)