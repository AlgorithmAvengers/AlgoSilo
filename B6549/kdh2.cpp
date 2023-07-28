#include <bits/stdc++.h>
using namespace std;

#define INF 999999
int n;
int hist[100005];
int seg[300005];
long long ans;

int leftChild(int node) {
    return node << 1;
}

int rightChild(int node) {
    return (node << 1) + 1;
}

int init(int node, int left, int right) {
	if(left == right) {
        return seg[node] = left;
    }
	int mid = (left + right) >> 1;
	int leftMinIdx = init(leftChild(node), left, mid);
	int rightMinIdx = init(rightChild(node), mid + 1, right);
	return seg[node] = hist[leftMinIdx] < hist[rightMinIdx] ? leftMinIdx : rightMinIdx;
}

int query(int node, int currLeft, int currRight, int queryLeft, int queryRight) {
	if(currRight < queryLeft || queryRight < currLeft) {
        return INF;
    }
	if(queryLeft <= currLeft && currRight <= queryRight) {
        return seg[node];
    }
	int currMid = (currLeft + currRight) >> 1;
	int leftMinIdx = query(leftChild(node), currLeft, currMid, queryLeft, queryRight);
	int rightMinIdx = query(rightChild(node), currMid + 1, currRight, queryLeft, queryRight);
	if(leftMinIdx >= INF) {
        return rightMinIdx;
    }
	else if(rightMinIdx >= INF) {
        return leftMinIdx;
    }
	else {
        return hist[leftMinIdx] < hist[rightMinIdx] ? leftMinIdx : rightMinIdx;
    }
}


void solve(int left, int right) {
	if(left > right) {
        return;
    }
	int minIdx = query(1, 0, n-1, left, right);
	ans = max(ans, (long long) hist[minIdx] * (right - left + 1));
	solve(left, minIdx - 1);
	solve(minIdx + 1, right);
}

int main() {
	while(true) {
		cin >> n;
		if(n == 0) {
            break;
        }
		for(int i=0; i<n; i++) {
			cin >> hist[i];
		}

        // segment tree를 만든다.
		init(1, 0, n-1);
        // 분할정복으로 최대 넓이를 찾는다.
        ans = 0;
		solve(0, n-1);
		cout << ans << endl;
	}
    return 0;
}