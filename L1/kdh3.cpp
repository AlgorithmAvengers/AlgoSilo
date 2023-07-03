#include <bits/stdc++.h>
using namespace std;
int main() {
    return 0;
}

// O(nlogn) (logn < 14)
// log1 + ... + logn = log(n!)
// O(log(n!)) = O(nlogn)
// https://www.reddit.com/r/algorithms/comments/6xi968/how_is_log_n_factorial_equal_to_omega_n_log_n/


class Solution {
public:
    vector<int> twoSum(vector<int>& nums, int target) {
        map<int, int> indexOf;
        for(int i=0; i<nums.size(); i++) {
            int need = target - nums[i];
            auto needIter = indexOf.find(need);
            if(needIter != indexOf.end()) {
                return {needIter -> second, i};
            }
            indexOf.insert(make_pair(nums[i], i));
        }
        return {};
    }
};