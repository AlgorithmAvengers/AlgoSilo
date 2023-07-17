import sys
def minTime():
    N, M = map(int, sys.stdin.readline().strip().split(' '))

    needTime = []
    for i in range(N):
        needTime.append(int(sys.stdin.readline().strip()))
    minNum = min(needTime) #제일 빨리하는 검사관
    start = minNum
    end = (M * minNum) #제일 빨리하는 검사관 한 명이 모두 다 할 때 걸리는 시간

    def check(div):
        result = 0
        for i in needTime:
            result += div // i
        return result


    while start <= end:
        mid = (start + end) // 2
        temp = check(mid)

        if temp == M:
            newStart = mid-minNum
            newEnd = mid
            while newStart + 1 < newEnd:
                mid = (newStart + newEnd) // 2
                temp = check(mid)
                # print(newStart, mid, newEnd, temp)
                if temp < M:
                    newStart = mid
                else:
                    newEnd = mid
            print(newEnd)
            return
        
        elif temp > M:
            end = mid-1
            
            
        else:
            start = mid + 1
    print(end+1)
minTime()