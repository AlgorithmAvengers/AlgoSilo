#include <bits/stdc++.h>
using namespace std;
int main() {
    return 0;
}

//1*9, 2*90, 3*900, 4*9000,
class Solution {
public:
    int findNthDigit(int n) {
        int first = 1;
        int step = 1;
        int num = 9;
        while(true) {
            int nextN = 0;
            if(step < 9) {
                nextN = n - step * num;
            }
            if(nextN <= 0) {
                int target = first + ((n-1) / step);
                int offset = (n-1) % step;
                for(int i=0; i<(step - 1 - offset); i++) {
                    target /= 10;
                }
                return target % 10;
            }
            n = nextN;
            first *= 10;
            step++;
            num *= 10;
        }
    }
};