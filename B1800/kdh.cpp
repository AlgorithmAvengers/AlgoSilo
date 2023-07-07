#include <bits/stdc++.h>
using namespace std;

#define INF 1000005
int n, p, k;
vector<pair<int, int>> cable[1005];
int maxCost = 0;
int ans = -1;

// dijkstra
// O((n+p)logn)
int isPossible(int budget) {
    int dist[1005] = {};
    for(int i=2; i<=n; i++) {
        dist[i] = INF;
    }

    priority_queue<pair<int, int>> q;
    q.push({0, 1});
    while(!q.empty()) {
        int curr = q.top().second;
        q.pop();
        for(int j=0; j<cable[curr].size(); j++) {
            int next = cable[curr][j].first;
            int cost = cable[curr][j].second;

            int newDist = dist[curr];
            if(cost > budget) {
                newDist++;
            }
            if(newDist < dist[next]) {
                dist[next] = newDist;
                q.push({-newDist, next});
            }
        }
    }
    return dist[n] <= k;
}

// 이진탐색
// O(log(maxCost) * (n+p)logn)
void f(int minCost, int maxCost) {
    if(minCost > maxCost) {
        return;
    }
    int budget = (minCost + maxCost) >> 1;
    if(isPossible(budget)) {
        ans = budget;
        f(minCost, budget - 1);
    } 
    else {
        f(budget + 1, maxCost);
    }
}


int main() {
    scanf("%d %d %d", &n, &p, &k);
    for(int i=0; i<p; i++) {
        int a, b, c;
        scanf("%d %d %d", &a, &b, &c);
        //인접리스트
        cable[a].push_back(make_pair(b, c));
        cable[b].push_back(make_pair(a, c));
        maxCost = max(maxCost, c);
    }
    f(0, maxCost);
    printf("%d", ans);
    return 0;
}