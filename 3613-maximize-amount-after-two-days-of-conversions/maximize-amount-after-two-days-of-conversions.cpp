class Solution {
private:
    unordered_map<string, vector<pair<string, double>>> makeAdjList(vector<vector<string>>& pairs, vector<double>& rates) {
        unordered_map<string, vector<pair<string, double>>> adjList;
        int totalPairs = pairs.size();

        for (int idx = 0; idx < totalPairs; idx++) {
            string src = pairs[idx][0];
            string dst = pairs[idx][1];
            double rate = rates[idx];
            adjList[src].push_back({dst, rate});
            adjList[dst].push_back({src, (1.0 / rate)});
        }

        return adjList;
    }

    void maxAmountDFS2(string& initialCurrency, string currCurrency, double currAmount, double& ans, unordered_map<string, vector<pair<string, double>>>& adj2, string parent) {
        if (currCurrency == initialCurrency) {
            ans = max(ans, currAmount);
        }

        vector<pair<string, double>> neighbourPairs = adj2[currCurrency];

        for (const pair<string, double>& currPair : neighbourPairs) {
            string neighbour = currPair.first;
            double rate = currPair.second;

            if (neighbour != parent) {
                maxAmountDFS2(initialCurrency, neighbour, currAmount * rate, ans, adj2, currCurrency);
            }
        }
    }

    void maxAmountDFS(string& initialCurrency, string currCurrency, double currAmount, double& ans, unordered_map<string, vector<pair<string, double>>>& adj1, unordered_map<string, vector<pair<string, double>>>& adj2, string parent) {
        vector<pair<string, double>> neighbourPairs = adj1[currCurrency];

        for (const pair<string, double>& currPair : neighbourPairs) {
            string neighbour = currPair.first;
            double rate = currPair.second;

            if (neighbour != parent) {
                maxAmountDFS2(initialCurrency, neighbour, currAmount * rate, ans, adj2, "");

                maxAmountDFS(initialCurrency, neighbour, currAmount * rate, ans, adj1, adj2, currCurrency);
            }
        }
    }

    double maxAmountUtil(string initialCurrency, unordered_map<string, vector<pair<string, double>>>& adj1, unordered_map<string, vector<pair<string, double>>>& adj2) {
        double ans = 1.0;
        double currAmount = 1.0;
        string parent = "";
        string currCurrency = initialCurrency;

        maxAmountDFS2(initialCurrency, currCurrency, currAmount, ans, adj2, parent);
        maxAmountDFS(initialCurrency, currCurrency, currAmount, ans, adj1, adj2, parent);
        return ans;
    }
public:
    double maxAmount(string initialCurrency, vector<vector<string>>& pairs1, vector<double>& rates1, vector<vector<string>>& pairs2, vector<double>& rates2) {
        unordered_map<string, vector<pair<string, double>>> adj1;
        unordered_map<string, vector<pair<string, double>>> adj2;

        adj1 = makeAdjList(pairs1, rates1);
        adj2 = makeAdjList(pairs2, rates2);

        return maxAmountUtil(initialCurrency, adj1, adj2);
    }
};