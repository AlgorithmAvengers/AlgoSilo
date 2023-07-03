#include <bits/stdc++.h>
using namespace std;

int main() {
    return 0;
}

bool cmp(int a, int b) {
    return a > b;
}

class Solution {
public:
    int maxSatisfaction(vector<int>& satisfaction) {
        sort(satisfaction.begin(), satisfaction.end(), cmp);
        int score = 0;
        int sum = 0;
        for(int i=0; i<satisfaction.size(); i++) {
            int newScore = score + satisfaction[i] + sum;
            if(newScore <= score) {
                break;
            }
            sum += satisfaction[i];
            score = newScore;
        }
        return score;
    }
};