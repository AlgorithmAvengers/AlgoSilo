#include <bits/stdc++.h>

int main() {
    int n;
    int x1, x2, r1, y1, y2, r2;

    scanf("%d", &n);
    for(int i=0; i<n; i++) {
        scanf("%d %d %d %d %d %d", &x1, &y1, &r1, &x2, &y2, &r2);
        int d = (x1 - x2) * (x1 - x2) + (y1 - y2) * (y1 - y2);
        int dsub = (r1 - r2) * (r1 - r2);
        int dadd = (r1 + r2) * (r1 + r2);

        if(d == 0 && r1 == r2 && r1 == 0) {
            printf("1\n");
        }
        else if(d == 0 && r1 == r2) {
            printf("-1\n");
        }
        else if(dsub < d && d < dadd) {
            printf("2\n");
        }
        else if(d == dsub || d == dadd) {
            printf("1\n");
        }
        else {
            printf("0\n");
        }
    }
    return 0;
}