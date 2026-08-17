#define pi pair<int, string>
class Solution {
public:
    struct Compare {
        bool operator()(const pi& pair1, const pi& pair2) {
            return pair1.first == pair2.first ? pair1.second < pair2.second : pair1.first > pair2.first;
        }
    };

    vector<string> topKFrequent(vector<string>& words, int k) {
        int totalWords = words.size();
        priority_queue<pi, vector<pi>, Compare> minHeap;
        vector<string> ans;
        unordered_map<string, int> wordFreqMap;

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
            string word = minHeap.top().second;
            minHeap.pop();

            ans.push_back(word);
        }

        reverse(ans.begin(), ans.end());
        return ans;
    }
};