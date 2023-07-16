class Solution:
    def networkDelayTime(self, times: List[List[int]], n: int, k: int) -> int:
        import heapq
        INF = 100000

        def dijkstra(k):
            q = []
            heapq.heappush(q, (0, k))
            distance[k] = 0
            while q:
                dist, now = heapq.heappop(q)
                if distance[now] < dist:
                    continue
                for link in times:
                    if link[0] != now:
                        continue
                    cost = dist + link[2]
                    if cost < distance[link[1]]:
                        distance[link[1]] = cost
                        heapq.heappush(q, (cost, link[1]))

        distance = [INF] * (n+1)

        dijkstra(k)

        count = 0
        max_distance = 0
        for d in distance:
            if d != 100000:
                count += 1
                max_distance = max(max_distance, d)

        if count < n:
            return -1
        else:
            return max_distance