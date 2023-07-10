#include <bits/stdc++.h>
using namespace std;

int n, m;
char board[25][25];
int ans = -1;

typedef struct {
    int moveCnt;
    int x1;
    int y1;
    int x2;
    int y2;
} BoardState;

int dx[4] = {1, 0, -1, 0};
int dy[4] = {0, 1, 0, -1};

bool isOut(int x, int y) {
    return x < 0 || x >= n || y < 0 || y >= m;
}

int main() {
    scanf("%d %d", &n, &m);
    for(int i=0; i<n; i++) {
        scanf("%s", board[i]);
    }
    int coinCnt = 0;
    BoardState initBoardState;
    initBoardState.moveCnt = 0;
    for(int i=0; i<n; i++) {
        for(int j=0; j<m; j++) {
            if(board[i][j] == 'o') {
                board[i][j] = '.';
                if(coinCnt == 0) {
                    initBoardState.x1 = i;
                    initBoardState.y1 = j;
                    coinCnt++;
                }
                else {
                    initBoardState.x2 = i;
                    initBoardState.y2 = j;
                    coinCnt++;
                    break;
                }
            }
        }
        if(coinCnt >= 2) {
            break;
        }
    }

    queue<BoardState> q;
    q.push(initBoardState);
    while(!q.empty()) {
        BoardState curr = q.front();
        q.pop();
        if(curr.moveCnt >= 10) {
            break;
        }
        curr.moveCnt++;
        for(int i=0; i<4; i++) {
            int nx1 = curr.x1 + dx[i];
            int ny1 = curr.y1 + dy[i];
            int nx2 = curr.x2 + dx[i];
            int ny2 = curr.y2 + dy[i];
            
            bool isOut1 = isOut(nx1, ny1);
            bool isOut2 = isOut(nx2, ny2);
            if((isOut1 && !isOut2) || (!isOut1 && isOut2)) {
                ans = curr.moveCnt;
                break;
            }
            else if(isOut1 && isOut2) {
                continue;
            }
            if(board[nx1][ny1] == '#') {
                nx1 = curr.x1;
                ny1 = curr.y1;
            }
            if(board[nx2][ny2] == '#') {
                nx2 = curr.x2;
                ny2 = curr.y2;
            }
            q.push({curr.moveCnt, nx1, ny1, nx2, ny2});
        }
        if(ans >= 0) {
            break;
        }
    }
    printf("%d", ans);
    return 0;
}