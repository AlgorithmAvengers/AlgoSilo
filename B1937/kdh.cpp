#include <bits/stdc++.h>
using namespace std;

int n;
int forest[505][505];
int score[505][505] = {};
int ans = 0;

int dx[4] = {1, 0, -1, 0};
int dy[4] = {0, 1, 0, -1};

int f(int x, int y, int prev) {
    if(x<0 || x>=n || y<0 || y>=n) {
        return 0;
    }
    if(forest[x][y] <= prev) {
        return 0;
    }
    if(!score[x][y]) {
        int res = 0;
        for(int i=0; i<4; i++) {
            int nx = x + dx[i];
            int ny = y + dy[i];
            res = max(res, f(nx, ny, forest[x][y]));
        }
        score[x][y] = res + 1;
    }
    return score[x][y];
}

int main() {
    cin >> n;
    for(int i=0; i<n; i++) {
        for(int j=0; j<n; j++) {
            cin >> forest[i][j];
        }
    }
    for(int i=0; i<n; i++) {
        for(int j=0; j<n; j++) {
            ans = max(ans, f(i, j, 0));
        }
    }
    cout << ans;
    return 0;
}