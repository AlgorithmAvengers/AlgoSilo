'''2
2
0 0
1000 0
1000 1000
2000 1000
2
0 0
1000 0
2000 1000
2000 2000'''
import queue
import sys

def distance(a, b, dic):
    return abs(dic[a][0] - dic[b][0]) + abs(dic[a][1] - dic[b][1])

def beer_walking():
    testcase = int(sys.stdin.readline().strip())
    testcase_list = []
    for tc in range(testcase):
        cs = int(sys.stdin.readline().strip())
        cs_list = {}
        for i in range(cs+2):
            cs_list[i] = list(map(int, sys.stdin.readline().strip().split(' ')))
        testcase_list.append((cs, cs_list))
    
    for cs, dic in testcase_list:
        bfs = queue.Queue()
        went = [False for _ in range(cs+2)]
        went[0] = True
        # print(distance(cs+1, 0, dic))
        if distance(cs+1, 0, dic) <= 1000:
            print("happy")
            continue
        for i in range(1, cs+1):
            if distance(i, 0, dic) <= 1000:
                bfs.put(i)
        while not bfs.empty():
            temp = bfs.get()
            if distance(cs+1, temp, dic) <= 1000:
                went[-1] = True
                print("happy")
                break
            went[temp] = True
            for i in range(1, cs+1):
                if (went[i] == False) and (distance(temp, i, dic) <= 1000):
                    bfs.put(i)
        if went[-1] == False:
            print("sad")

beer_walking()
