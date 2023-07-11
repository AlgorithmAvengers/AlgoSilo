#include <bits/stdc++.h>
using namespace std;

int n, m;
vector<int> conn[50005];
int parent[50005] = {};
int depth[50005] = {};
int ans;


void dfs(int curr, int prev, int d) {
    parent[curr] = prev;
    depth[curr] = d;
    for(int i=0; i<conn[curr].size(); i++) {
        int next = conn[curr][i];
        if(parent[next]) {
            continue;
        }
        dfs(next, curr, d+1);
    }
}

void find(int a, int b) {
    if(a == b) {
        ans = a;
        return;
    }
    if(depth[a] < depth[b]) {
        find(a, parent[b]);
    }
    else if(depth[a] > depth[b]) {
        find(parent[a], b);
    }
    else {
        find(parent[a], parent[b]);
    }
} 

int main() {
    scanf("%d", &n);
    for(int i=0; i<n-1; i++) {
        int a, b;
        scanf("%d %d", &a, &b);
        conn[a].push_back(b);
        conn[b].push_back(a);
    }
    dfs(1, -1, 1);
    scanf("%d", &m);
    for(int i=0; i<m; i++) {
        int a, b;
        scanf("%d %d", &a, &b);
        find(a, b);
        printf("%d\n", ans);
    }
    return 0;
}