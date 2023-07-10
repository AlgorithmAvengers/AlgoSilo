INF = 1000001

def choose_vertex(dist, found):
    min = INF
    minpos = -1
    for i in range(len(dist)):
        if dist[i]<min and found[i]==False:
            min = dist[i]
            minpos = i
    return minpos

def shortest_path(vtx, adj, record, k):
    dist = list(adj[0])
    path = [0]*n
    found = [False]*n
    found[0] = True
    dist[0] = 0

    for i in range(n):
        u = choose_vertex(dist, found)
        found[u] = True
        for w in range(n):
            if not found[w]:

                if dist[u] + adj[u][w] < dist[w]:
                    dist[w] = dist[u] + adj[u][w]
                    path[w] = u
                    record[w].append(adj[u][w])
                    freeline = sorted(record[w].copy())[-k:]

    return dist

if __name__ == ‘main’:
    n, p, k = map(int, sys.stdin.readline().split())
    vtx = list(range(1, n+1))
    vtx.remove(0)
    weight = [[INF]*n for i in range(n)]
    record = [[] for i in range(n)]
    for i in range(p):
        a, b, c = map(int, sys.stdin.readline().split())
        weight[a-1][b-1] = c
        weight[b-1][a-1] = c