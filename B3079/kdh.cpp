#include <bits/stdc++.h>
using namespace std;

// 최소 소요시간부터 최대 소요시간 사이에서 가능한 답을 이분탐색

#define INF 1000000005
int n, m;
long long t[100005];
long long minT = INF;
long long maxT = 0;
long long ans;

void f(long long left, long long right) {
    if(left > right) {
        return;
    }
    long long mid = (left + right) >> 1;
    long long sum = 0;
    for(int i=0; i<n; i++) {
        sum += mid / t[i];
    }
    if(sum >= m) {
        ans = mid;
        f(left, mid - 1);
    }
    else {
        f(mid + 1, right);
    }
}

int main() {
    scanf("%d %d", &n, &m);
    for(int i=0; i<n; i++) {
        scanf("%d", &t[i]);
        minT = min(minT, t[i]);
        maxT = max(maxT, t[i]);
    }
    long long ceil = (m / n) + ((m % n) > 0);
    f(minT * ceil, maxT * ceil);
    printf("%lld", ans);
    return 0;
}