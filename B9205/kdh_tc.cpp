#include <bits/stdc++.h>
using namespace std;

// 1000보다 가까운 정점만 dfs나 bfs로 순회해서 도달가능한지 파악

int t;
int n;
int xs[105], ys[105];
bool visited[105];

string tcFileName = "tc5";
int randInt(int min, int max) {
    return min + rand() % ((max+1) - min);
}

int main() {
    srand(time(NULL));
    ofstream fin;
    fin.open(tcFileName + ".in");
    ofstream fout;
    fout.open(tcFileName + ".out");

    t = randInt(1, 50);
    fin << t << "\n";
    // scanf("%d", &t);
    for(int i=0; i<t; i++) {
        n = randInt(0, 100);
        fin << n << "\n";
        // scanf("%d", &n);
        xs[0] = randInt(-3276, 3276);
        ys[0] = randInt(-3276, 3276);
        // xs[0] = randInt(-32768, 32767);
        // ys[0] = randInt(-32768, 32767);
        fin << xs[0] << " " << ys[0] << "\n";
        // scanf("%d %d", &xs[0], &ys[0]);
        for(int j=1; j<=n; j++) {
            xs[j] = randInt(-3276, 3276);
            ys[j] = randInt(-3276, 3276);
            // xs[j] = randInt(-3276, 32767);
            // ys[j] = randInt(-32768, 32767);
            fin << xs[j] << " " << ys[j] << "\n";
            // scanf("%d %d", &xs[j], &ys[j]);
        }
        xs[n+1] = randInt(-3276, 3276);
        ys[n+1] = randInt(-3276, 3276);
        // xs[n+1] = randInt(-32768, 32767);
        // ys[n+1] = randInt(-32768, 32767);
        fin << xs[n+1] << " " << ys[n+1] << "\n";
        // scanf("%d %d", &xs[n+1], &ys[n+1]);
        for(int j=0; j<=n+1; j++) {
            visited[j] = false;
        }

        queue<int> q;
        q.push(0);
        while(!q.empty()) {
            int curr = q.front();
            q.pop();
            visited[curr] = true;
            for(int next=0; next<=n+1; next++) {
                if(visited[next]) {
                    continue;
                }
                int dist = abs(xs[curr] - xs[next]) + abs(ys[curr] - ys[next]);
                if(dist > 1000) {
                    continue;
                }
                q.push(next);
            }
        }
        if(visited[n+1]) {
            fout << "happy\n";
            // printf("happy\n");
        }
        else {
            fout << "sad\n";
            // printf("sad\n");
        }
    }

    return 0;
}