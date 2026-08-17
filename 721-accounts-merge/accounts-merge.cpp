class Solution {
private:
    unordered_map<string, string> parent;
    unordered_map<string, int> rank;
    unordered_map<string, unordered_set<string>> neighbours;

    string find(string x) {
        if (x == parent[x]) return x;
        return parent[x] = find(parent[x]);
    }   

    bool unite(string a, string b) {
        string x_parent = find(a);
        string y_parent = find(b);

        if (x_parent == y_parent) {
            return false;
        }

        if (rank[x_parent] > rank[y_parent]) {
            parent[y_parent] = x_parent;

            for (const string& str : neighbours[y_parent]) {
                neighbours[x_parent].insert(str);
            }
        }
        else if (rank[x_parent] < rank[y_parent]) {
            parent[x_parent] = y_parent;

            for (const string& str : neighbours[x_parent]) {
                neighbours[y_parent].insert(str);
            }
        }
        else {
            parent[y_parent] = x_parent;

            for (const string& str : neighbours[y_parent]) {
                neighbours[x_parent].insert(str);
            }
            rank[x_parent]++;
        }

        return true;
    }
public:
    vector<vector<string>> accountsMerge(vector<vector<string>>& accounts) {
        // mapping of email to name 
        unordered_map<string, string> emailToName;
        vector<vector<string>> ans;

        for (const vector<string>& account : accounts) {
            string name = account[0];

            for (int idx = 1; idx < account.size(); idx++) {
                string email = account[idx];
                emailToName[email] = name;
                rank[email] = 1;
                parent[email] = email;
                neighbours[email].insert(email);
            }
        }

        for (const vector<string>& account : accounts) {
            string name = account[0];

            for (int idx = 1; idx < account.size() - 1; idx++) {
                unite(account[idx], account[idx + 1]);
            }
        }

        for (const pair<string, string>& parentPair : parent) {
            if (parentPair.first == parentPair.second) {
                vector<string> account;
                string name = emailToName[parentPair.first];
                account.push_back(name);

                for (const string& str : neighbours[parentPair.first]) {
                    account.push_back(str);
                }

                sort(account.begin() + 1, account.end());
                ans.push_back(account);
            }
        }

        return ans;
    }
};