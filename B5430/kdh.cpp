#include <bits/stdc++.h>
using namespace std;

int t, n;
string p, numsString;
int nums[100005] = {};
int front, rear;
bool isReversed;

void makeNums() {
    if(numsString.length() <= 2) {
        return;
    }
    for(int i=0; i<numsString.length(); i++) {
        switch (numsString[i]) {
        case '[':
            nums[rear] = 0;
            break;
        case ']':
        case ',':
            rear++;
            nums[rear] = 0;
            break;
        default:
            nums[rear] *= 10;
            nums[rear] += numsString[i] - '0';
            break;
        }
    }
}

bool runP() {
    for(int i=0; i<p.length(); i++) {
        switch (p[i]) {
        case 'R':
            isReversed = !isReversed;
            break;
        case 'D':
            if(front >= rear) {
                return false;
            }
            if(isReversed) {
                rear--;
            }
            else {
                front++;
            }
            break;
        }
    }
    return true;
}

void printNums() {
    cout << "[";
    if(isReversed) {
        for(int i=rear-1; i>=front; i--) {
            if(i != rear-1) {
                cout << ",";
            }
            cout << nums[i];
        }
    }
    else {
        for(int i=front; i<rear; i++) {
            if(i != front) {
                cout << ",";
            }
            cout << nums[i];
        }
    }
    cout << "]" << endl;
}

int main() {
    cin >> t;
    for(int i=0; i<t; i++) {
        cin >> p;
        cin >> n;
        cin >> numsString;

        front = 0;
        rear = 0;
        isReversed = false;

        makeNums();
        if(runP()) {
            printNums();
        }
        else {
            cout << "error" << endl;
        }
    }
    return 0;
}