#include <bits/stdc++.h>
using namespace std;
int main() {
    return 0;
}

class Solution {
public:
    bool isValidSudoku(vector<vector<char>>& board) {
    	for(int i=0; i<9; i++) {
    		bool chk[9] = {};
    		for(int j=0; j<9; j++) {
    			if(board[i][j] == '.') {
    				continue;
    			}
    			if(chk[board[i][j] - '1']) {
    				return false;
                }
                chk[board[i][j] - '1'] = true;
    		}
        }
        for(int i=0; i<9; i++) {
    		bool chk[9] = {};
    		for(int j=0; j<9; j++) {
    			if(board[j][i] == '.') {
    				continue;
    			}
    			if(chk[board[j][i] - '1']) {
    				return false;
                }
                chk[board[j][i] - '1'] = true;
    		}
        }
        for(int i=0; i<9; i+=3) {
            for(int j=0; j<9; j+=3) {
 		   		bool chk[9] = {};
 		   		for(int p=0; p<3; p++) {
 		   			for(int q=0; q<3; q++) {
   		 				if(board[i+p][j+q] == '.') {
	    					continue;
    					}
    					if(chk[board[i+p][j+q] - '1']) {
    						return false;
                        }
                        chk[board[i+p][j+q] - '1'] = true;
                    }
    			}
    		}
        }
        return true;
    }
};