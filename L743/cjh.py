class Solution:
    def networkDelayTime(self, times: List[List[int]], n: int, k: int) -> int:
        # 각 노드에서 출발하는 directed graph 형태로 나타내는 것
        adjlst = {i:[] for i in range(1, n+1)}
        for u, v, w in times:
            adjlst[u].append((v, w))
        
        # min_time이라는 heapq에 tuple 형태로 각 노드로 가는데에 걸리는 시간과 그 노드 번호를 저장
        min_time = [(0, k)]
        # min_time을 측정하기 위한 기준 정하기
        t = 0
        # 방문한 노드를 기억하기 위한 set
        visited = set()
        
        # min_time 안에 무언가 남아있다면 아직 탐색할 노드가 남아있다는 뜻
        while min_time:
            #heapq의 특성상, pop을 하면 첫 번째 값의 최소값을 무조건 먼저 내보냄
            w1, n1 = heapq.heappop(min_time)

            # 이미 방문한 노드라면 해당 루프 건너뜀
            if n1 in visited:
                continue

            # 방문한 노드를 기록
            visited.add(n1)

            # 최대 시간을 기억함
            t = max(t, w1)

            # 현재 출발한 노드에서 아직 방문하지 않은 노드 방문 + 방문까지 걸린 시간 기억하여 저장
            for n2, w2 in adjlst[n1]:
                if n2 not in visited:
                    heapq.heappush(min_time, (w1+w2, n2))
        
        # 모든 노드 방문 가능하면 t를 반환하고, 아니라면 -1
        if len(visited) != n:
            return -1
        else:
            return t