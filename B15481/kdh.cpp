#include <bits/stdc++.h>
using namespace std;

int n, m;
pair<int, pair<int, int>> edges[200005];
vector<int> conn[200005];

bool isInMst[200005] = {};
vector<int> mstConn[200005];
long long mstCost = 0;
priority_queue<pair<int, int>> q;
int visitCnt = 0;
bool visited[200005] = {};

int parentEdgeIdx[200005];
int depth[200005] = {};

void visit(int node) {
    visited[node] = true;
    visitCnt++;
    for(int i=0; i<conn[node].size(); i++) {
        int edgeIdx = conn[node][i];
        int w = edges[edgeIdx].first;
        q.push({-w, edgeIdx});
    }
}

void prim() {
    visit(1);
    while(visitCnt < n) {
        int edgeIdx = q.top().second;
        q.pop();
        int u = edges[edgeIdx].second.first;
        int v = edges[edgeIdx].second.second;
        int w = edges[edgeIdx].first;
        if(visited[u] && visited[v]) {
            continue;
        }
        int newNode = visited[u] ? v : u;
        isInMst[edgeIdx] = true;
        mstConn[u].push_back(edgeIdx);
        mstConn[v].push_back(edgeIdx);
        mstCost += w;
        visit(newNode);
    }
}

void dfs(int curr, int d) {
    depth[curr] = d;
    for(int i=0; i<mstConn[curr].size(); i++) {
        int edgeIdx = mstConn[curr][i];
        int u = edges[edgeIdx].second.first;
        int v = edges[edgeIdx].second.second;
        int next = u == curr ? v : u;
        if(depth[next]) {
            continue;
        }
        parentEdgeIdx[next] = edgeIdx;
        dfs(next, d+1);
    }
}

int findMax(int node1, int node2) {
    if(node1 == node2) {
        return 0;
    }
    if(depth[node1] < depth[node2]) {
        return findMax(node2, node1);
    }
    int edgeIdx1 = parentEdgeIdx[node1];
    int u1 = edges[edgeIdx1].second.first;
    int v1 = edges[edgeIdx1].second.second;
    int w1 = edges[edgeIdx1].first;
    int parent1 = node1 == u1 ? v1 : u1;
    if(depth[node1] > depth[node2]) {
        return max(w1, findMax(parent1, node2));
    }
    int edgeIdx2 = parentEdgeIdx[node2];
    int u2 = edges[edgeIdx2].second.first;
    int v2 = edges[edgeIdx2].second.second;
    int w2 = edges[edgeIdx2].first;
    int parent2 = node2 == u2 ? v2 : u2;
    return max(w1, max(w2, findMax(parent1, parent2)));
}

int main() {
    scanf("%d %d", &n, &m);
    for(int i=0; i<m; i++) {
        int u, v, w;
        scanf("%d %d %d", &u, &v, &w);
        edges[i] = {w, {u, v}};
        conn[u].push_back(i);
        conn[v].push_back(i);
    }

    prim();
    dfs(1, 1);

    for(int i=0; i<m; i++) {
        if(isInMst[i]) {
            printf("%lld\n", mstCost);
            continue;
        }
        int u = edges[i].second.first;
        int v = edges[i].second.second;
        int w = edges[i].first;
        printf("%lld\n", mstCost - findMax(u, v) + w);
    }
    return 0;
}