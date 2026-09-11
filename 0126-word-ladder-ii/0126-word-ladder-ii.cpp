#include <vector>
#include <string>
#include <unordered_set>
#include <unordered_map>
#include <queue>
#include <algorithm>

using namespace std;

class Solution {
    unordered_map<string, vector<string>> adj;
    vector<vector<string>> ans;
    string bWord;
    
    // Phase 2: DFS to reconstruct paths from the adjacency map
    void dfs(string word, vector<string>& path) {
        if (word == bWord) {
            vector<string> temp = path;
            reverse(temp.begin(), temp.end()); // Reverse because we built it backwards
            ans.push_back(temp);
            return;
        }
        
        for (string& parent : adj[word]) {
            path.push_back(parent);
            dfs(parent, path);
            path.pop_back(); // Backtrack memory reuse
        }
    }

public:
    vector<vector<string>> findLadders(string beginWord, string endWord, vector<string>& wordList) {
        unordered_set<string> dict(wordList.begin(), wordList.end());
        bWord = beginWord;
        
        if (dict.find(endWord) == dict.end()) return {};
        
        queue<string> q;
        q.push(beginWord);
        dict.erase(beginWord);
        
        // Tracks the minimum steps to reach each word to prevent cycles
        unordered_map<string, int> steps;
        steps[beginWord] = 0;
        
        // Phase 1: BFS to build the graph
        while (!q.empty()) {
            int size = q.size();
            bool found = false;
            
            for (int i = 0; i < size; i++) {
                string curr = q.front();
                q.pop();
                int currSteps = steps[curr];
                
                if (curr == endWord) found = true;
                
                string temp = curr;
                for (int j = 0; j < curr.length(); j++) {
                    char original = temp[j]; // Store original character
                    
                    for (char ch = 'a'; ch <= 'z'; ch++) {
                        temp[j] = ch; // In-place string mutation
                        
                        if (dict.count(temp)) {
                            // If this is the shortest path to this word, map it to its parent
                            if (!steps.count(temp) || steps[temp] == currSteps + 1) {
                                adj[temp].push_back(curr);
                                
                                // Only push to queue if it's the first time seeing this word
                                if (!steps.count(temp)) {
                                    steps[temp] = currSteps + 1;
                                    q.push(temp);
                                }
                            }
                        }
                    }
                    temp[j] = original; // Backtrack the character string
                }
            }
            if (found) break; // Stop BFS early once the shortest path level is finished
        }
        
        vector<string> path;
        path.push_back(endWord);
        dfs(endWord, path);
        
        return ans;
    }
};