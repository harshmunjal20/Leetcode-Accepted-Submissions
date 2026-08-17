class Solution {
public:
    struct Compare {
        bool operator()(const pair<int, string>& pair1, const pair<int, string>& pair2) const {
            return pair1.first == pair2.first ? pair1.second < pair2.second : pair1.first > pair2.first;
        }
    };

    vector<string> topKFrequent(vector<string>& words, int k) {
        vector<string> ans;
        unordered_map<string, int> wordFreqMap;
        priority_queue<pair<int, string>, vector<pair<int, string>>, Compare> minHeap;

        for (const string& word : words) {
            wordFreqMap[word]++;
        }

        for (const pair<string, int>& wordFreqPair : wordFreqMap) {
            string word = wordFreqPair.first;
            int freq = wordFreqPair.second;

            minHeap.push({freq, word});
            if (minHeap.size() > k) {
                minHeap.pop();
            }
        }
        
        while (!minHeap.empty()) {
            int freq = minHeap.top().first;
            string word = minHeap.top().second;
            minHeap.pop();

            ans.push_back(word);
        }

        reverse(ans.begin(), ans.end());
        return ans;
    }
};