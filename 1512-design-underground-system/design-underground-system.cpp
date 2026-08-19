class UndergroundSystem {
private:
    unordered_map<string, unordered_map<string, vector<int>>> startToEndTimes;
    unordered_map<int, pair<string, int>> idToStation; 
public:
    UndergroundSystem() {
        startToEndTimes.clear();
        idToStation.clear();
    }
    
    void checkIn(int id, string stationName, int t) {
        idToStation[id] = {stationName, t};
    }
    
    void checkOut(int id, string stationName, int t) {
        pair<string, int> beginToTime = idToStation[id];
        idToStation.erase(id);
        string start = beginToTime.first;
        int prevTime = beginToTime.second;
        startToEndTimes[start][stationName].push_back(t - prevTime);
    }
    
    double getAverageTime(string startStation, string endStation) {
        vector<int> times = startToEndTimes[startStation][endStation];
        int sz = times.size();
        double averageTime = 0;
        int totalTime = 0;
        
        for (int idx = 0; idx < sz; idx++) {
            totalTime += times[idx];
        }

        return (double)totalTime / sz;
    }
};

/**
 * Your UndergroundSystem object will be instantiated and called as such:
 * UndergroundSystem* obj = new UndergroundSystem();
 * obj->checkIn(id,stationName,t);
 * obj->checkOut(id,stationName,t);
 * double param_3 = obj->getAverageTime(startStation,endStation);
 */