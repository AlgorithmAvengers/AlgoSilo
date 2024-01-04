#include <bits/stdc++.h>
using namespace std;

int n;
int arr[100005];
int m;
int a, b, c;
int seg[400005];

int makeSeg(int curr, int l, int r) {
	if(l == r) {
		return seg[curr] = (arr[l] % 2 == 0);
	}
	int m = (l + r) >> 1;
	return seg[curr] = makeSeg(curr<<1, l, m) + makeSeg((curr<<1)+1, m+1, r);
}

int updateSeg(int curr, int l, int r, int i, int d) {
	if(i < l || r < i) {
		return seg[curr];
	}
	if(l == r) {
		return seg[curr] = d;
	}
	int m = (l + r) >> 1;
	return seg[curr] = updateSeg(curr<<1, l, m, i, d) + updateSeg((curr<<1)+1, m+1, r, i, d);
}

int resultSeg(int curr, int l, int r, int s, int e)  {
	if(e < l || r < s) {
		return 0;
	}
	if(s <= l && r <= e) {
		return seg[curr];
	}
	if(l == r) {
		return 0;
	}
	int m = (l + r) >> 1;
	return resultSeg(curr<<1, l, m, s, e) + resultSeg((curr<<1)+1, m+1, r, s, e);
}

int main() {
	ios_base::sync_with_stdio(false); cin.tie(nullptr); cout.tie(nullptr);
	cin >> n;
	for(int i=1; i<=n; i++) {
		cin >> arr[i];
	}
	makeSeg(1, 1, n);
	cin >> m;
	for(int i=0; i<m; i++) {
		cin >> a >> b >> c;
		switch(a) {
		case 1:
      		arr[b] = c;
			updateSeg(1, 1, n, b, c%2 == 0);
			break;
		case 2:
			cout << resultSeg(1, 1, n, b, c) << "\n";
			break;
		case 3:
			cout << (c - b + 1 - resultSeg(1, 1, n, b, c)) << "\n";
			break;
		default:
			break;
		}
	}
	return 0;
}