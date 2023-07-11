#include <bits/stdc++.h>
using namespace std;

int n;
int t;
int lis[40005];
int cnt = 0;

void f(int left, int right) {
    if(left >= right) {
        lis[left] = t;
        return;
    }
    int mid = (left + right) >> 1;
    if(lis[mid] < t) {
        f(mid + 1, right);
    }
    else {
        f(left, mid);
    }
}

int main() {
    scanf("%d", &n);
    for(int i=1; i<=n; i++) {
        scanf("%d", &t);
        if(cnt == 0 || lis[cnt-1] < t) {
            lis[cnt++] = t;
            continue;
        }
        f(0, cnt);
    }
    printf("%d", cnt);
    return 0;
}