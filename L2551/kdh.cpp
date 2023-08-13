#include <bits/stdc++.h>
using namespace std;
int main() {
    return 0;
}

class Solution {
public:
    long long putMarbles(vector<int>& weights, int k) {
        for(int i=0; i<weights.size()-1; i++) {
			weights[i] = weights[i] + weights[i+1];
		}
		sort(weights.begin(), weights.end() - 1);
		long long ans = 0;
		for(int i=0; i<k-1; i++) {
			ans += weights[weights.size() - 2 - i] - weights[i];
		}
		return ans;
    }
};