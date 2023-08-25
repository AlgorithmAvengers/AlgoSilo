import sys
# from collections import deque

N = int(sys.stdin.readline().strip())#testcase 숫자
ans = []
for n in range(N):
    # stack = deque()
    func = sys.stdin.readline().strip()
    num = int(sys.stdin.readline().strip()) #array 길이
    if num > 1:
        arr = sys.stdin.readline().strip().strip("[]").split(",")
        arr = list(map(int, arr))
    elif num == 1:
        arr = [int(sys.stdin.readline().strip().strip("[]"))]
    else:
        temp = sys.stdin.readline().strip()
        arr = []
    isReverse = False
    isError = False
    front, back = 0, 0
    for fun in range(len(func)):
        if func[fun] == 'R':
            isReverse = not isReverse
        else:
            if len(arr) == 0:
                ans.append("error")
                isError = True
                break
            if isReverse == False:
                front += 1
            else:
                back += 1
    if isError == True:
        continue
    if front + back > num:
        ans.append("error")
        continue
    elif back == 0:
        arr= arr[front:]
    else:
        arr = arr[front:-1*back]
    
    if isReverse == True and len(arr) > 1:
        arr = arr[::-1]
    ans.append(arr)
for i in ans:
    print(i)
    # print("\n")
