#include <bits/stdc++.h>

int main() {
    int n;
    int a;
    int arr[45] = {0, 1};
    scanf("%d", &n);
    for(int i=0; i<n; i++) {
        scanf("%d", &a);
        if(a == 0) {
            printf("1 0\n");
            continue;
        }
        
        for(int j=2; j<=a; j++) {
            arr[j] = arr[j-1] + arr[j-2];
        }

        printf("%d %d\n", arr[a-1], arr[a]);
    }

    return 0;
}