// 1 2 3 4 5 6
// 3 2 5 6 1 4

// 1 3 5 1: 3
// 2 2: 1
// 4 6 4: 2
// 6

#include <bits/stdc++.h>
using namespace std;

int n;
int shuf[20005];
int visited[20005] = {};
set<int> loops;
int ans = 1;

int main() {
    scanf("%d", &n);
    for(int i=1; i<=n; i++) {
        scanf("%d", &shuf[i]);
    }
    for(int i=1; i<=n; i++) {
        if(visited[i]) {
            continue;
        }
        int cnt = 0;
        int curr = i;
        while(true) {
            cnt++;
            visited[curr] = 1;
            curr = shuf[curr];
            if(curr == i) {
                break;
            }
        }
        if(cnt == 1) {
            continue;
        }
        loops.insert(cnt);
    }
    for(int x : loops) {
        ans = lcm(ans, x);
    }
    printf("%d", ans);
    return 0;
}