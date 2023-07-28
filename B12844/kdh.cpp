#include <bits/stdc++.h>
using namespace std;

int arr[500005];
int seg[500005 * 4];
int lazy[500005 * 4] = {};

void makeSeg(int curr, int l, int r) {
    if(l == r) {
        seg[curr] = arr[l];
        return;
    }
    int mid = (l + r) >> 1;
    makeSeg(curr << 1, l, mid);
    makeSeg((curr << 1) | 1, mid+1, r);
    seg[curr] = seg[curr << 1] ^ seg[(curr << 1) | 1];
}

void propagate(int curr, int l, int r) {
    if(!lazy[curr]) {
        return;
    }
    if(l < r) {
        lazy[curr << 1] ^= lazy[curr];
        lazy[(curr << 1) | 1] ^= lazy[curr];
    }
    if((r - l + 1) % 2) {
        seg[curr] ^= lazy[curr];
    }
    lazy[curr] = 0;
}

void query1(int curr, int l, int r, int k, int queryL, int queryR) {
    propagate(curr, l, r);
    if(r < queryL || queryR < l) {
        return;
    }
    if(queryL <= l && r <= queryR) {
        lazy[curr] ^= k;
        propagate(curr, l, r);
        return;
    }
    int mid = (l + r) >> 1;
    query1(curr << 1, l, mid, k, queryL, queryR);
    query1((curr << 1) | 1, mid+1, r, k, queryL, queryR);
    seg[curr] = seg[curr << 1] ^ seg[(curr << 1) | 1];
}

int query2(int curr, int l, int r, int queryL, int queryR) {
    propagate(curr, l, r);
    if(r < queryL || queryR < l) {
        return 0;
    }
    if(queryL <= l && r <= queryR) {
        return seg[curr];
    }
    int mid = (l + r) >> 1;
    int lRes = query2(curr << 1, l, mid, queryL, queryR);
    int rRes = query2((curr << 1) | 1, mid+1, r, queryL, queryR);
    return lRes ^ rRes;
}

int main() {
    int n, m, op, queryL, queryR, k;
    cin >> n;
    for(int i=0; i<n; i++) {
        cin >> arr[i];
    }
    makeSeg(1, 0, n-1);
    cin >> m;
    for(int i=0; i<m; i++) {
        cin >> op;
        if(op == 1) {
            cin >> queryL >> queryR >> k;
            query1(1, 0, n-1, k, queryL, queryR);
        }
        else {
            cin >> queryL >> queryR;
            cout << query2(1, 0, n-1, queryL, queryR) << endl;
        }
    }
    return 0;
}