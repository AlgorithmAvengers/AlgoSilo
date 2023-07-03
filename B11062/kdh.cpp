#include <bits/stdc++.h>
using namespace std;

int t;
int n;
int score[1005];
int dp[1005][1005][2] = {};

void f(int s, int e, int turn) {
    if(s > e) {
        return;
    }
    if(dp[s][e][turn] != 0) {
        return;
    }
    f(s+1, e, 1-turn);
    f(s, e-1, 1-turn);
    int s1 = score[s] + min(dp[s+2][e][turn], dp[s+1][e-1][turn]);
    int s2 = score[e] + min(dp[s+1][e-1][turn], dp[s][e-2][turn]);
    dp[s][e][turn] = max(s1, s2);
}

int main() {
    scanf("%d", &t);
    for(int i=0; i<t; i++) {
        scanf("%d", &n);
        for(int j=0; j<n; j++) {
            scanf("%d", &score[j]);
        }
        for(int j=0; j<n; j++) {
            for(int k=0; k<n; k++) {
                dp[j][k][0] = 0;
                dp[j][k][1] = 0;
            }
        }
        f(0, n-1, 0);
        printf("%d\n", dp[0][n-1][0]);
    }
    return 0;
}