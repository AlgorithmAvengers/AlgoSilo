#include <bits/stdc++.h>
using namespace std;

int n;
vector<int> conn[10005];
int visited[10005] = {};
int dp[10005][2] = {};

void f(int curr) {
    visited[curr] = 1;
    for(int i=0; i<conn[curr].size(); i++) {
        int next = conn[curr][i];
        if(!visited[next]) {
            f(next);
            dp[curr][0] = dp[curr][0] + dp[next][1];
            dp[curr][1] = dp[curr][1] + max(dp[next][0], dp[next][1]);
        }
    }
}


int main() {
    scanf("%d", &n);
    for(int i=1; i<=n; i++) {
        scanf("%d", &dp[i][0]);
    }
    for(int i=0; i<n-1; i++) {
        int a, b;
        scanf("%d %d", &a, &b);
        conn[a].push_back(b);
        conn[b].push_back(a);
    }

    f(1);
    printf("%d", max(dp[1][0], dp[1][1]));
    return 0;
}