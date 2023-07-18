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
struct TreeNode *maxNode;
struct TreeNode *wrong1;
struct TreeNode *wrong2;

void swap(struct TreeNode *node1, struct TreeNode *node2) {
    int temp = node1->val;
    node1->val = node2->val;
    node2->val = temp;
}

void dfs(struct TreeNode *curr) {
    if(curr == nullptr) {
        return;
    }
    dfs(curr->left);
    if(maxNode == nullptr) {
        maxNode = curr;
    }
    else if(maxNode->val < curr->val) {
        maxNode = curr;
    }
    else if(wrong1 == nullptr) {
        wrong1 = maxNode;
        wrong2 = curr;
    }
    else {
        wrong2 = curr;
    }
    dfs(curr->right);
}


class Solution {
public:
    void recoverTree(TreeNode* root) {
        maxNode = nullptr;
        wrong1 = nullptr;
        wrong2 = nullptr;
        dfs(root);
        swap(wrong1, wrong2);
    }
};