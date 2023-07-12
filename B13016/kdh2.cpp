#include <bits/stdc++.h>
using namespace std;

// 처음에 생각한 풀이 (틀렸습니다 뜨는데 이유를 모르겠음)

int n;
vector<pair<int, int>> conn[50005];
bool visited[50005] = {};
vector<pair<int, int>> children[50005];
int childMaxDist[50005] = {};
// int childSecondMaxDist[50005] = {};
int maxDistFromFirst[50005];
int maxDistFromLast[50005];
int tempMaxDist;
int D[50005];

void dfs1(int curr) {
    visited[curr] = true;
    for(int i=0; i<conn[curr].size(); i++) {
        int next = conn[curr][i].first;
        if(visited[next]) {
            continue;
        }
        int dist = conn[curr][i].second;
        children[curr].push_back({next, dist});
        dfs1(next);
        childMaxDist[curr] = max(childMaxDist[curr], dist + childMaxDist[next]);
        // if(childMaxDist[curr] < dist + childMaxDist[next]) {
        //     childSecondMaxDist[curr] = childMaxDist[curr];
        //     childMaxDist[curr] = dist + childMaxDist[next];
        // }
        // else if(childSecondMaxDist[curr] < dist + childMaxDist[next]) {
        //     childSecondMaxDist[curr] = dist + childMaxDist[next];
        // }
    }
}

void dfs2(int curr, int parentMaxDist) {
    D[curr] = max(childMaxDist[curr], parentMaxDist);
    tempMaxDist = 0;
    for(int i=0; i<children[curr].size(); i++) {
        int child = children[curr][i].first;
        int dist = children[curr][i].second;
        tempMaxDist = max(tempMaxDist, dist + childMaxDist[child]);
        maxDistFromFirst[i] = tempMaxDist;
    }
    tempMaxDist = 0;
    for(int i=children[curr].size()-1; i>=0; i--) {
        int child = children[curr][i].first;
        int dist = children[curr][i].second;
        tempMaxDist = max(tempMaxDist, dist + childMaxDist[child]);
        maxDistFromLast[i] = tempMaxDist;
    }
    for(int i=0; i<children[curr].size(); i++) {
        int child = children[curr][i].first;
        int dist = children[curr][i].second;
        int max0 = i-1 >= 0 ? maxDistFromFirst[i-1] : 0;
        int max1 = i+1 < children[curr].size() ? maxDistFromLast[i+1] : 0;
        int otherChildMaxDist = max(max0, max1);
        // int otherChildMaxDist = (childMaxDist[curr] == childMaxDist[child] + dist) ? childSecondMaxDist[curr] : childMaxDist[curr];
        dfs2(child, dist + max(parentMaxDist, otherChildMaxDist));
    }
}

int main() {
    scanf("%d", &n);
    for(int i=0; i<n-1; i++) {
        int a, b, c;
        scanf("%d %d %d", &a, &b, &c);
        conn[a].push_back({b, c});
        conn[b].push_back({a, c});
    }
    dfs1(1);
    dfs2(1, 0);
    for(int i=1; i<=n; i++) {
        printf("%d\n", D[i]);
    }
    return 0;
}