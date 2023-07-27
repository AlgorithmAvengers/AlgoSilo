#include <bits/stdc++.h>
using namespace std;

int n;
int hist[100005];
stack<pair<int, int>> stk;

int main() {
    while(true) {
        cin >> n;
        if(n == 0) {
            break;
        }
        long long ans = 0;
        for(int i=0; i<n; i++) {
            cin >> hist[i];
        }

        for(int i=0; i<n; i++) {
            int minIdx = i;
            while(!stk.empty() && stk.top().first > hist[i]) {
                minIdx = stk.top().second;
                long long area = (long long) stk.top().first * (i - minIdx);
                stk.pop();
                ans = max(ans, area);
            }
            if(stk.empty() || stk.top().first < hist[i]) {
                stk.push({hist[i], minIdx});
            }
        }
        while (!stk.empty()) {
            long long area = (long long) stk.top().first * (n - stk.top().second);
            stk.pop();
            ans = max(ans, area);
        }

        cout << ans << endl;
    }
    return 0;
}