#include <bits/stdc++.h>
using namespace std;

#define LIMIT 100005
int n, k;
queue<pair<int, int>> q;
bool visited[LIMIT] = {};

int main() {
    cin >> n >> k;
    q.push({0, n});
    while(!q.empty()) {
        int sec = q.front().first;
        int pos = q.front().second;
        q.pop();
        if(pos < 0 || pos >= LIMIT || visited[pos]) {
            continue;
        }
        visited[pos] = true;
        if(pos == k) {
            cout << sec;
            break;
        }
        if(pos < k) {
            q.push({sec + 1, 2 * pos});
        }
        q.push({sec + 1, pos - 1});
        q.push({sec + 1, pos + 1});
    }
    return 0;
}