#include <bits/stdc++.h>
using namespace std;

#define LIMIT 40005

int n;
int t;
vector<int> possible;
bool chk[LIMIT * 2] = {};

int chkIdx(int idx) {
    return idx + LIMIT;
}

int main() {
    possible.push_back(0);
    chk[chkIdx(0)] = true;

    cin >> n;
    for(int i=0; i<n; i++) {
        cin >> t;
        int currSize = possible.size();
        for(int j=0; j<currSize; j++) {
            int p1 = possible[j] + t;
            int p2 = possible[j] - t;
            int p1Idx = chkIdx(p1);
            int p2Idx = chkIdx(p2);
            if(0 <= p1Idx && p1Idx < LIMIT*2 && !chk[p1Idx]) {
                possible.push_back(p1);
                chk[p1Idx] = true;
            }
            if(0 <= p2Idx && p2Idx < LIMIT*2 && !chk[p2Idx]) {
                possible.push_back(p2);
                chk[p2Idx] = true;
            }
        }
    }
    cin >> n;
    for(int i=0; i<n; i++) {
        cin >> t;
        if(chk[chkIdx(t)]) {
            cout << "Y ";
        }
        else {
            cout << "N ";
        }
    }
    return 0;
}