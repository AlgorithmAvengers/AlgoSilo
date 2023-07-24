#include <bits/stdc++.h>
using namespace std;

int n;
string A;
bool swt[20][20] = {};
bool light[20][20] = {};
vector<pair<bool, pair<int, int>>> zombies;

int dir = 0;
int dx[4] = {1, 0, -1, 0};
int dy[4] = {0, 1, 0, -1};
int x=1, y=1;

int main() {
    cin >> n;
    cin >> A;
    for(int i=1; i<=n; i++) {
        string t;
        cin >> t;
        for(int j=1; j<=n; j++) {
            if(t[j-1] == 'Z') {
                zombies.push_back({false, {i, j}});
            }
            else if(t[j-1] == 'S') {
                swt[i][j] = true;
            }
        }
    }
    for(int i=0; i<A.size(); i++) {
        if(A[i] == 'F') {
            int nx = x + dx[dir];
            int ny = y + dy[dir];
            if(1<=nx && nx<=n && 1<=ny && ny<=n) {
                x = nx;
                y = ny;
                if(swt[x][y]) {
                    for(int j=x-1; j<=x+1; j++) {
                        for(int k=y-1; k<=y+1; k++) {
                            light[j][k] = true;
                        }
                    }
                    swt[x][y] = false;
                }
            }
        }
        else if(A[i] == 'L') {
            dir = (dir + 1) % 4;
        }
        else if(A[i] == 'R') {
            dir = (dir + 3) % 4;
        }
        for(int j=0; j<zombies.size(); j++) {
            int zx = zombies[j].second.first;
            int zy = zombies[j].second.second;
            if(x == zx && y == zy && !light[x][y]) {
                cout << "Aaaaaah!";
                return 0;
            }
            if(zombies[j].first) {
                if(zx-1 < 1) {
                    zombies[j] = {false, {zx, zy}};
                }
                else {
                    zx--;
                    zombies[j] = {true, {zx, zy}};
                }
            }
            else {
                if(zx+1 > n) {
                    zombies[j] = {true, {zx, zy}};
                }
                else {
                    zx++;
                    zombies[j] = {false, {zx, zy}};
                }
            }
            if(x == zx && y == zy && !light[x][y]) {
                cout << "Aaaaaah!";
                return 0;
            }
        }
    }
    cout << "Phew...";
    return 0;
}