#include <bits/stdc++.h>
using namespace std;

#define INF 999
int n;
int health[3] = {};
int dp[65][65][65];
int damage[6][3] = {
	{9, 3, 1},
	{9, 1, 3},
	{3, 9, 1},
	{3, 1, 9},
	{1, 9, 3},
	{1, 3, 9},
};

int f() {
	int healthCopy[3] = {health[0], health[1], health[2]};
	sort(healthCopy, healthCopy + 3);
	int h0 = max(healthCopy[0], 0);
	int h1 = max(healthCopy[1], 0);
	int h2 = max(healthCopy[2], 0);

	if(dp[h0][h1][h2] >= INF) {
		for(int i=0; i<6; i++) {
			for(int j=0; j<3; j++) {
				health[j] -= damage[i][j];
			}
			dp[h0][h1][h2] = min(dp[h0][h1][h2], 1 + f());
			for(int j=0; j<3; j++) {
				health[j] += damage[i][j];
			}
		}
	}
	return dp[h0][h1][h2];
}

int main() {
    cin >> n;
    for(int i=0; i<n; i++) {
        cin >> health[i];
    }
	
    sort(health, health+3);
    for(int i=0; i<=health[0]; i++) {
		for(int j=0; j<=health[1]; j++) {
			for(int k=0; k<=health[2]; k++) {
				dp[i][j][k] = INF;
			}
		}
	}
    dp[0][0][0] = 0;

    cout << f();
    return 0;
}