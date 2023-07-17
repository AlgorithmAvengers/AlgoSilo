#include <bits/stdc++.h>
using namespace std;

// 1000보다 가까운 정점만 dfs나 bfs로 순회해서 도달가능한지 파악

int t;
int n;
int xs[105], ys[105];
bool visited[105];

int main() {
    scanf("%d", &t);
    for(int i=0; i<t; i++) {
        scanf("%d", &n);
        scanf("%d %d", &xs[0], &ys[0]);
        for(int j=1; j<=n; j++) {
            scanf("%d %d", &xs[j], &ys[j]);
        }
        scanf("%d %d", &xs[n+1], &ys[n+1]);
        for(int j=0; j<=n+1; j++) {
            visited[j] = false;
        }

        queue<int> q;
        q.push(0);
        while(!q.empty()) {
            int curr = q.front();
            q.pop();
            visited[curr] = true;
            for(int next=0; next<=n+1; next++) {
                if(visited[next]) {
                    continue;
                }
                int dist = abs(xs[curr] - xs[next]) + abs(ys[curr] - ys[next]);
                if(dist > 1000) {
                    continue;
                }
                q.push(next);
            }
        }
        if(visited[n+1]) {
            printf("happy\n");
        }
        else {
            printf("sad\n");
        }
    }

    return 0;
}