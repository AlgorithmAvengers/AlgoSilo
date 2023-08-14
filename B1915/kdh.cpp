#include <bits/stdc++.h>
using namespace std;

int n, m;
string s;
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
            box[i][j] = min(box[i-1][j-1], min(box[i][j-1], box[i-1][j])) + 1;
            if(box[i][j] > maxLen) {
                maxLen = box[i][j];
            }
        }
    }
    cout << (maxLen * maxLen);
    return 0;
}