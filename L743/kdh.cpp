#include <bits/stdc++.h>
using namespace std;
int main() {
    return 0;
}

// 다익스트라 후 최대 딜레이 시간 찾기

#define INF 1000000
int dist[105];

class Solution {
public:
    int networkDelayTime(vector<vector<int>>& times, int n, int k) {
        for(int i=1; i<=n; i++) {
            dist[i] = INF;
        }

        priority_queue<pair<int, int>> q;
        q.push({0, k});
        dist[k] = 0;
        while(!q.empty()) {
            int curr = q.top().second;
            q.pop();
            for(int i=0; i<times.size(); i++) {
                if(times[i][0] != curr) {
                    continue;
                }
                int next = times[i][1];
                int time = times[i][2];
                int newDist = dist[curr] + time;
                if(newDist < dist[next]) {
                    dist[next] = newDist;
                    q.push({-newDist, next});
                }
            }
        }
        int ans = 0;
        for(int i=1; i<=n; i++) {
            ans = max(ans, dist[i]);
        }
        if(ans >= INF) {
            return -1;
        }
        return ans;
    }
};