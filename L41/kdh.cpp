#include <bits/stdc++.h>
using namespace std;
int main() {
    return 0;
}

class Solution {
public:
    int firstMissingPositive(vector<int>& nums) {
        for(int i=0; i<nums.size(); i++) {
            if(nums[i] < 0) {
                nums[i] = 0;
            }
        }
        for(int i=0; i<nums.size(); i++) {
            int curr = nums[i];
            while(0 <= curr-1 && curr-1 < nums.size()) {
                int next = nums[curr-1];
                nums[curr-1] = -1;
                curr = next;
            }
        }
        for(int i=0; i<nums.size(); i++) {
            if(nums[i] != -1) {
                return i + 1;
            }
        }
        return nums.size() + 1;
    }
};