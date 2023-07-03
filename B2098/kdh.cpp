#include <bits/stdc++.h>
using namespace std;

#define INF 1e9
int n;
int w[20][20];
int dp[20][1 << 16] = {};
int complete;

void f(int curr, int idx) {
    if(dp[curr][idx] != 0) {
        return;
    }
    if(idx == complete) {
        dp[curr][idx] = w[curr][0] == 0 ? INF : w[curr][0];
        return;
    }

    dp[curr][idx] = INF;
    for(int next=0; next<n; next++) {
        if(w[curr][next] == 0) {
            continue;
        }
        int bit = 1 << next;
        int visited = idx & bit;
        if(visited) {
            continue;
        }
        int nextIdx = idx | bit;
        f(next, nextIdx);
        dp[curr][idx] = min(dp[curr][idx], dp[next][nextIdx] + w[curr][next]);
    }
}

int main() {
    scanf("%d", &n);
    for(int i=0; i<n; i++) {
        for(int j=0; j<n; j++) {
            scanf("%d", &w[i][j]);
        }
    }
    complete = (1 << n) - 1;
    f(0, 1);
    printf("%d", dp[0][1]);
    return 0;
}