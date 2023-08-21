#include <bits/stdc++.h>
using namespace std;

int n, m;
int grid[1005][1005];
int dx[4] = {1, 0, -1, 0};
int dy[4] = {0, 1, 0, -1};
queue<pair<int, pair<int, int>>> q;

int main() {
    cin >> m >> n;
    for(int i=0; i<n; i++) {
    	for(int j=0; j<m; j++) {
    		cin >> grid[i][j];
    		if(grid[i][j] == 1) {
    			grid[i][j] = 0;
    			q.push({1, {i, j}});
    		}
        }
    }
    while(!q.empty()) {
    	int day = q.front().first;
    	int x = q.front().second.first;
    	int y = q.front().second.second;
    	q.pop();
    	if(x < 0 || x > n-1 || y < 0 || y > m-1) {
    		continue;
    	}
    	if(grid[x][y] == -1) {
    		continue;
    	}
    	if(grid[x][y] > 0 && grid[x][y] <= day) {
    		continue;
    	}
    	grid[x][y] = day;
    	for(int i=0; i<4; i++) {
    		q.push({day+1, {x + dx[i], y + dy[i]}});
    	}
    }
    int ans = 0;
    for(int i=0; i<n; i++) {
    	for(int j=0; j<m; j++) {
    		if(grid[i][j] == 0) {
    			cout << "-1";
    			return 0;
    		}
    		ans = max(ans, grid[i][j]);
        }
    }
    cout << ans - 1;
    return 0;
}