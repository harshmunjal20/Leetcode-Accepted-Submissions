class DSU {
private:
    vector<int> parent;
    vector<int> rank;
public:
    DSU(int totalSize) {
        parent.resize(totalSize);
        rank.resize(totalSize, 1);

        for (int idx = 0; idx < totalSize; idx++) {
            parent[idx] = idx;
        }
    }
    
    int find(int val) {
        if (val == parent[val]) return val;
        return parent[val] = find(parent[val]);
    }

    bool unite(int x, int y) {
        int parent_x = find(x);
        int parent_y = find(y);

        if (parent_x == parent_y) return false;

        if (rank[parent_x] > rank[parent_y]) {
            parent[parent_y] = parent_x;
        }
        else if (rank[parent_x] < rank[parent_y]) {
            parent[parent_x] = parent_y;
        }
        else {
            parent[parent_y] = parent_x;
            rank[parent_x]++;
        }

        return true;
    }
};

class Solution {
public:
    vector<vector<string>> accountsMerge(vector<vector<string>>& accounts) {
        int totalAccounts = accounts.size();
        DSU* dsu = new DSU(totalAccounts);
        vector<vector<string>> ans;
        unordered_map<string, int> emailToIdxMap;
        
        for (int idx = 0; idx < totalAccounts; idx++) {
            string name = accounts[idx][0];

            for (int i = 1; i < accounts[idx].size(); i++) {
                string email = accounts[idx][i];

                if (emailToIdxMap.count(email) == 0) {
                    emailToIdxMap[email] = idx;
                }
                else {
                    dsu->unite(idx, emailToIdxMap[email]);
                }
            }
        }

        unordered_map<int, unordered_set<string>> idxToEmailsMap;

        for (int idx = 0; idx < totalAccounts; idx++) {
            string name = accounts[idx][0];
            int parentIdx = dsu->find(idx);

            for (int i = 1; i < accounts[idx].size(); i++) {
                string email = accounts[idx][i];
                idxToEmailsMap[parentIdx].insert(email);
            }
        }

        for (const pair<int, unordered_set<string>>& idxToEmails : idxToEmailsMap) {
            vector<string> account;
            int idx = idxToEmails.first;
            account.push_back(accounts[idx][0]);
            account.insert(account.end(), idxToEmails.second.begin(), idxToEmails.second.end());
            sort(account.begin() + 1, account.end());
            ans.push_back(account);
        }

        return ans;
    }
};