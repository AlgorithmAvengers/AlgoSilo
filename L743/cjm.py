import queue

class Solution:
    def networkDelayTime(self, times: List[List[int]], n: int, k: int) -> int:
        went = [False] * (n+1)
        dist = [float("inf")] * (n+1)
        dist[0] = 0
        went[0] = True
        base = [[float("inf")]*(n+1) for _ in range(n+1)]
        for i in times:
            base[i[0]][i[1]] = i[2]
        
        bfs = queue.Queue(2**n)
        bfs.put(k)
        dist[k] = 0
        while not bfs.empty():
            temp = bfs.get()
            if went[temp] == True:
                for i in range(n+1):
                    if dist[temp] + base[temp][i] < dist[i]:
                        dist[i] = dist[temp] + base[temp][i]
            else:
                went[temp] = True
                for i in range(n+1):
                    if base[temp][i] != float("inf"):
                        bfs.put(i)
                        if dist[temp] + base[temp][i] < dist[i]:
                            dist[i] = dist[temp] + base[temp][i]
        if sum(dist) < float("inf"):
            return max(dist)
        else:
            return -1


