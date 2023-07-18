#include <bits/stdc++.h>
using namespace std;
int main() {
    return 0;
}

// Definition for a binary tree node.
struct TreeNode {
    int val;
    TreeNode *left;
    TreeNode *right;
    TreeNode() : val(0), left(nullptr), right(nullptr) {}
    TreeNode(int x) : val(x), left(nullptr), right(nullptr) {}
    TreeNode(int x, TreeNode *left, TreeNode *right) : val(x), left(left), right(right) {}
};


// SUBMIT
bool isWrong;

void swap(struct TreeNode *node1, struct TreeNode *node2) {
    int temp = node1->val;
    node1->val = node2->val;
    node2->val = temp;
}

void dfs(struct TreeNode *curr, struct TreeNode *leftBound, struct TreeNode *rightBound) {
    if(curr == nullptr) {
        return;
    }
    if(leftBound != nullptr && curr->val < leftBound->val) {
        swap(curr, leftBound);
        isWrong = true;
        return;
    }
    else if(rightBound != nullptr && rightBound->val < curr->val) {
        swap(curr, rightBound);
        isWrong = true;
        return;
    }
    dfs(curr->left, leftBound, curr);
    dfs(curr->right, curr, rightBound);
}

class Solution {
public:
    void recoverTree(TreeNode* root) {
        isWrong = true;
        while(isWrong) {
            isWrong = false;
            dfs(root, nullptr, nullptr);
        }
    }
};