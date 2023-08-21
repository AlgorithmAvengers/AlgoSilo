#include <bits/stdc++.h>
using namespace std;

#define INF 999999999
int t;
int k;
int files[505];
int sum[505] = {};
int D[505][505];

int f(int left, int right) {
    if(left == right) {
        return 0;
    }
    if(!D[left][right]) {
        D[left][right] = INF;
        for(int i=left; i<right; i++) {
            D[left][right] = min(D[left][right], f(left, i) + f(i+1, right));
        }
        D[left][right] += sum[right] - sum[left-1];
    }
    return D[left][right];
}

int main() {
    cin >> t;
    for(int idx=0; idx<t; idx++) {
        cin >> k;
        for(int i=1; i<=k; i++) {
            cin >> files[i];
            sum[i] = sum[i-1] + files[i];
            for(int j=1; j<=k; j++) {
                D[i][j] = 0;
            }
        }
        cout << f(1, k) << endl;
    }
    return 0;
}