#include <bits/stdc++.h>
using namespace std;

#define INF 20010;
int t;
int n, w;
int enemy[2][10005];
int dp[5][10005];
// dp[case][i]: 각 경우의 1~i구역에 쓰이는 최소 소대수
// case 0: 0번칸만 이전칸과 연결됨
// case 1: 1번칸만 이전칸과 연결됨
// case 2: 둘다 이전칸과 연결됨
// case 3: 0번칸과 1번칸이 서로 연결됨
// case 4: 둘다 아무것에 연결되지 않음

void process() {
    for(int k=2; k<=n; k++) {
        int isAble0 = (enemy[0][k] + enemy[0][k-1]) <= w;
        int isAble1 = (enemy[1][k] + enemy[1][k-1]) <= w;
        int isAble2 = isAble0 && isAble1;
        int isAble3 = (enemy[0][k] + enemy[1][k]) <= w;
        int tempMin = min(dp[0][k-1], min(dp[1][k-1], min(dp[2][k-1], min(dp[3][k-1], dp[4][k-1]))));
        dp[0][k] = isAble0 ? 1 + min(dp[1][k-1], dp[4][k-1]) : INF;
        dp[1][k] = isAble1 ? 1 + min(dp[0][k-1], dp[4][k-1]) : INF;
        dp[2][k] = isAble2 ? dp[4][k-1] : INF;
        dp[3][k] = isAble3 ? 1 + tempMin : INF;
        dp[4][k] = 2 + tempMin;
    }
}

int main() {
    scanf("%d", &t);
    for(int i=0; i<t; i++) {
        scanf("%d %d", &n, &w);
        for(int j=0; j<2; j++) {
            for(int k=1; k<=n; k++) {
                scanf("%d", &enemy[j][k]);
            }
        }
        if(n == 1) {
            printf("%d\n", (enemy[0][1] + enemy[1][1]) <= w ? 1 : 2);
            continue;
        }
        int ans = INF;
        int isAble0 = (enemy[0][1] + enemy[0][n]) <= w;
        int isAble1 = (enemy[1][1] + enemy[1][n]) <= w;
        int isAble2 = isAble0 && isAble1;
        int isAble3 = (enemy[0][1] + enemy[1][1]) <= w;
        if(isAble0) {
            dp[0][1] = 1;
            dp[1][1] = INF;
            dp[2][1] = INF;
            dp[3][1] = INF;
            dp[4][1] = INF;
            process();
            int tempMin = min(dp[1][n], dp[4][n]);
            ans = min(ans, tempMin);
        }
        if(isAble1) {
            dp[0][1] = INF;
            dp[1][1] = 1;
            dp[2][1] = INF;
            dp[3][1] = INF;
            dp[4][1] = INF;
            process();
            int tempMin = min(dp[0][n], dp[4][n]);
            ans = min(ans, tempMin);
        }
        if(isAble2) {
            dp[0][1] = INF;
            dp[1][1] = INF;
            dp[2][1] = 0;
            dp[3][1] = INF;
            dp[4][1] = INF;
            process();
            int tempMin = dp[4][n];
            ans = min(ans, tempMin);
        }
        if(isAble3) {
            dp[0][1] = INF;
            dp[1][1] = INF;
            dp[2][1] = INF;
            dp[3][1] = 1;
            dp[4][1] = INF;
            process();
            int tempMin = min(dp[0][n], min(dp[1][n], min(dp[2][n], min(dp[3][n], dp[4][n]))));
            ans = min(ans, tempMin);
        }
        dp[0][1] = INF;
        dp[1][1] = INF;
        dp[2][1] = INF;
        dp[3][1] = INF;
        dp[4][1] = 2;
        process();
        int tempMin = min(dp[0][n], min(dp[1][n], min(dp[2][n], min(dp[3][n], dp[4][n]))));
        ans = min(ans, tempMin);

        printf("%d\n", ans);
    }
    return 0;
}