#include <bits/stdc++.h>
using namespace std;
int main() {
    return 0;
}

int D[305][305];

class Solution {
public:
    int maxCoins(vector<int>& nums) {
		nums.insert(nums.begin(), 1);
		nums.push_back(1);

		for(int i=0; i<nums.size(); i++) {
			for(int j=0; j<nums.size(); j++) {
				D[i][j] = 0;
			}
		}

		for(int size=3; size<=nums.size(); size++) {
			for(int left=0; left<=nums.size()-size; left++) {
				int right = left + size - 1;
				for(int i=left+1; i<=right-1; i++) {
					int score = D[left][i] + D[i][right] + nums[left] * nums[i] * nums[right];
					D[left][right] = max(D[left][right], score);
				}
			}
		}
		return D[0][nums.size()-1];
    }
};
