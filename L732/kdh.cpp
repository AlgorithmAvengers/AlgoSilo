#include <bits/stdc++.h>
using namespace std;
int main() {
    return 0;
}

class Node {
public:
    Node *left = nullptr;
    Node *right = nullptr;
    int time;
    bool isStart;

    Node(int _time, bool _isStart) {
        time = _time;
        isStart = _isStart;
    }
};

class MyCalendarThree {
public:
    Node *root = nullptr;
    int maxBook = 0;
    int temp;
    MyCalendarThree() {}

    // O(logn) (average)
    Node *insert(Node *curr, Node *newNode) {
        if(curr == nullptr) {
            return newNode;
        }
        if(curr->time < newNode->time) {
            curr->right = insert(curr->right, newNode);
        }
        else if(curr->time > newNode->time) {
            curr->left = insert(curr->left, newNode);
        }
        else if(!newNode->isStart) {
            curr->left = insert(curr->left, newNode);
        }
        else {
            curr->right = insert(curr->right, newNode);
        }
        return curr;
    }

    // O(n)
    void getMaxBook(Node *curr) {
        if(curr == nullptr) {
            return;
        }
        getMaxBook(curr->left);
        if(curr->isStart) {
            temp++;
            maxBook = max(maxBook, temp);
        }
        else {
            temp--;
        }
        getMaxBook(curr->right);
    }
    
    int book(int startTime, int endTime) {
        root = insert(root, new Node(startTime, true));
        root = insert(root, new Node(endTime, false));
        temp = 0;
        getMaxBook(root);
        return maxBook;
    }
};