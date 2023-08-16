#include <bits/stdc++.h>
using namespace std;
int main() {
    return 0;
}

int f(vector<int>& nums) {
	if(nums.size() <= 0) {
		return 0;
	}
	int res = 0;
	for(int i=0; i<nums.size(); i++) {
		int temp = nums[i];
		int score = nums[i];
		if(i > 0) {
			score *= nums[i-1];
		}
		if(i < nums.size()-1) {
			score *= nums[i+1];
		}
		nums.erase(nums.begin() + i);
		res = max(score + f(nums), res);
		nums.insert(nums.begin() + i, temp);
	}
	return res;
}

class Solution {
public:
    int maxCoins(vector<int>& nums) {
		return f(nums);
    }
};