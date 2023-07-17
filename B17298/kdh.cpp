#include <bits/stdc++.h>
using namespace std;

int n;
int arr[1000005];
int ans[1000005];
stack<int> s;

int main() {
    scanf("%d", &n);
    for(int i=0; i<n; i++) {
        scanf("%d", &arr[i]);
    }
    for(int i=n-1; i>=0; i--) {
        while(!s.empty() && s.top() <= arr[i]) {
            s.pop();
        }
        if(s.empty()) {
            ans[i] = -1;
        }
        else {
            ans[i] = s.top();
        }
        s.push(arr[i]);
    }
    for(int i=0; i<n; i++) {
        printf("%d ", ans[i]);
    }
    return 0;
}