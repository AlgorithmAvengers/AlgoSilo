#include <bits/stdc++.h>
using namespace std;

int n;
int height[55];
int visible[55][55] = {};
int ans = 0;

int main() {
    cin >> n;
    for(int i=1; i<=n; i++) {
        cin >> height[i];
    }
    for(int i=1; i<=n; i++) {
        for(int j=i+1; j<=n; j++) {
            bool v = true;
            for(int k=i+1; k<=j-1; k++) {
                double a = (double)(height[j] - height[i]) / (j - i);
                double h = a * (k - i) + height[i];
                v = v && (h > height[k]);
            }
            visible[i][j] = v;
            visible[j][i] = v;
        }
    }
    for(int i=1; i<=n; i++) {
        int cnt = 0;
        for(int j=1; j<=n; j++) {
            if(i != j && visible[i][j]) {
                cnt++;
            }
        }
        ans = max(ans, cnt);
    }
    cout << ans;
    return 0;
}