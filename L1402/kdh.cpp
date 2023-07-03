#include <bits/stdc++.h>
using namespace std;

int main() {
    return 0;
}

class Solution {
public:
    int partitionString(string s) {
        int chk[30] = {};
        int cnt = 0;
        for(int i=0; i<s.size(); i++) {
            int idx = s[i] - 'a';
            if(chk[idx]) {
                cnt++;
                for(int j=0; j<30; j++) {
                    chk[j] = 0;
                }
            }
            chk[idx] = 1;
        }
        return cnt + 1;
    }
};