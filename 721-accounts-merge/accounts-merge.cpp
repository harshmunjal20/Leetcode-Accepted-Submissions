class Solution {
private:
    vector<int> parent;
    vector<int> rank;
    unordered_map<int, unordered_set<int>> neighbours;

    int find(int x) {
        if (x == parent[x]) return x;
        return parent[x] = find(parent[x]);
    }   

    bool unite(int a, int b) {
        int x_parent = find(a);
        int y_parent = find(b);

        if (x_parent == y_parent) {
            return false;
        }

        if (rank[x_parent] > rank[y_parent]) {
            parent[y_parent] = x_parent;

            for (const int& num : neighbours[y_parent]) {
                neighbours[x_parent].insert(num);
            }
        }
        else if (rank[x_parent] < rank[y_parent]) {
            parent[x_parent] = y_parent;

            for (const int& num : neighbours[x_parent]) {
                neighbours[y_parent].insert(num);
            }
        }
        else {
            parent[y_parent] = x_parent;

            for (const int& num : neighbours[y_parent]) {
                neighbours[x_parent].insert(num);
            }
            rank[x_parent]++;
        }

        return true;
    }
public:
    vector<vector<string>> accountsMerge(vector<vector<string>>& accounts) {
        // mapping of email to name 
        unordered_map<int, string> idToName;
        vector<vector<string>> ans;
        int id = 0;
        unordered_map<string, int> emailToId;
        unordered_map<int, string> idToEmail;

        for (const vector<string>& account : accounts) {
            string name = account[0];

            for (int idx = 1; idx < account.size(); idx++) {
                string email = account[idx];

                if (emailToId.count(email) == 0) {
                    idToName[id] = name;
                    neighbours[id].insert(id);
                    emailToId[email] = id;
                    idToEmail[id] = email;
                    id++;
                }
            }
        }

        rank.resize(id + 1, 1);
        parent.resize(id + 1);
        
        for (int count = 0; count < id; count++) {
            parent[count] = count;
        }

        for (const vector<string>& account : accounts) {
            string name = account[0];

            for (int idx = 1; idx < account.size() - 1; idx++) {
                unite(emailToId[account[idx]], emailToId[account[idx + 1]]);
            }
        }

        for (int idx = 0; idx < parent.size(); idx++) {
            if (idx == parent[idx]) {
                vector<string> account;
                string name = idToName[idx];
                account.push_back(name);

                for (const int& num : neighbours[idx]) {
                    account.push_back(idToEmail[num]);
                }

                sort(account.begin() + 1, account.end());
                ans.push_back(account);
            }
        }

        return ans;
    }
};