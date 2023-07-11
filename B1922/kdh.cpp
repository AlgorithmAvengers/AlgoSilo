#include <bits/stdc++.h>
using namespace std;

int n, m;
vector<pair<int, int>> conn[1005];
bool visited[1005];
int visitCnt = 0;
priority_queue<pair<int, int>> q;
int ans = 0;

int main() {
    scanf("%d %d", &n, &m);
    for(int i=0; i<m; i++) {
        int a, b, c;
        scanf("%d %d %d", &a, &b, &c);
        conn[a].push_back({b, c});
        conn[b].push_back({a, c});
    }
    visited[1] = true;
    visitCnt++;
    for(int i=0; i<conn[1].size(); i++) {
        int next = conn[1][i].first;
        int cost = conn[1][i].second;
        q.push({-cost, next});
    }
    while(visitCnt < n) {
        int cost = -q.top().first;
        int newNode = q.top().second;
        q.pop();
        if(visited[newNode]) {
            continue;
        }
        visited[newNode] = true;
        visitCnt++;
        ans += cost;
        for(int i=0; i<conn[newNode].size(); i++) {
            int next = conn[newNode][i].first;
            int cost = conn[newNode][i].second;
            q.push({-cost, next});
        }
    }
    printf("%d", ans);
    return 0;
}