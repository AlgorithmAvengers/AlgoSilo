#include <bits/stdc++.h>
using namespace std;
int main() {
    return 0;
}

// O(nlogn) (logn < 14)
// nlogn + n

bool cmp(pair<int, int> a, pair<int, int> b) {
    return a.first < b.first;
}

class Solution {
public:
    vector<int> twoSum(vector<int>& nums, int target) {
        vector<pair<int, int>> numIdxs;
        for(int i=0; i<nums.size(); i++) {
            numIdxs.push_back(make_pair(nums[i], i));
        }
        sort(numIdxs.begin(), numIdxs.end(), cmp);
        int p = 0, q = numIdxs.size() - 1;
        while(p < q) {
            int sum = numIdxs[p].first + numIdxs[q].first;
            if(sum == target) {
                return {numIdxs[p].second, numIdxs[q].second};
            }
            else if(sum < target) {
                p++;
            }
            else {
                q--;
            }
        }
        return {};
    }
};