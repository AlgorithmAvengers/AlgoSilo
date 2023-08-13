#include <bits/stdc++.h>
using namespace std;

int n, m;
string s;
int row[1005][1005] = {};
int col[1005][1005] = {};
int box[1005][1005] = {};
int maxLen = 0;

int main() {
    cin >> n >> m;
    for(int i=1; i<=n; i++) {
        cin >> s;
        for(int j=1; j<=m; j++) {
            if(s[j-1] == '0') {
                continue;
            }
            row[i][j] = row[i][j-1] + 1;
            col[i][j] = col[i-1][j] + 1;
            box[i][j] = min(box[i-1][j-1], min(row[i][j-1], col[i-1][j])) + 1;
            if(box[i][j] > maxLen) {
                maxLen = box[i][j];
            }
        }
    }
    cout << (maxLen * maxLen);
    return 0;
}