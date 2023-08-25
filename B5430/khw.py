from collections import deque
import sys

input = sys.stdin.readline

t = int(input())
 
for i in range(t):
    func = input()
    n = int(input())
    target = deque(input()[1:-1].split(','))
 
    for i in func:
        if i == 'R':
            target.reverse()
        elif i == "D":
            if len(target) == 0:
                break
            else:
                target.popleft()
                
    if len(target) == 0:
        print('error')
    else:
        print(list(target))