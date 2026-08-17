class Solution {
public:
    struct Compare {
        bool operator()(const pair<int, string>& pair1, const pair<int, string>& pair2) const {
            return pair1.first == pair2.first ? pair1.second > pair2.second : pair1.first < pair2.first;
        }
    };

    vector<string> topKFrequent(vector<string>& words, int k) {
        vector<string> ans;
        unordered_map<string, int> wordsFreqMap;
        priority_queue<pair<int, string>, vector<pair<int, string>>, Compare> maxHeap;

        for (const string& word : words) {
            wordsFreqMap[word]++;
        }

        for (const pair<string, int>& wordFreqPair : wordsFreqMap) {
            string word = wordFreqPair.first;
            int freq = wordFreqPair.second;
            maxHeap.push({freq, word});
        }
        
        while (!maxHeap.empty() && k > 0) {
            int freq = maxHeap.top().first;
            string word = maxHeap.top().second;
            maxHeap.pop();

            ans.push_back(word);
            k--;
        }

        return ans;
    }
};