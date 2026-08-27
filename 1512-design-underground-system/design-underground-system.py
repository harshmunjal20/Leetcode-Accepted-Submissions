class UndergroundSystem(object):

    def __init__(self):
        # id mapped with startStation and time
        # startStation mapped with endstation mapped with list of times taken
        self.idStartStationTimeMap = defaultdict()
        self.startEndTimesMap = defaultdict(lambda : defaultdict(list))

    def checkIn(self, id, stationName, t):
        """
        :type id: int
        :type stationName: str
        :type t: int
        :rtype: None
        """
        self.idStartStationTimeMap[id] = (stationName, t)
        

    def checkOut(self, id, stationName, t):
        """
        :type id: int
        :type stationName: str
        :type t: int
        :rtype: None
        """
        startStationAndTime = self.idStartStationTimeMap[id]
        startStation = startStationAndTime[0]
        timeStart = startStationAndTime[1]
        self.startEndTimesMap[startStation][stationName].append(t - timeStart)
        

    def getAverageTime(self, startStation, endStation):
        """
        :type startStation: str
        :type endStation: str
        :rtype: float
        """
        sum , count = 0.0, 0.0

        for time in self.startEndTimesMap[startStation][endStation]:
            sum += time
            count += 1

        return sum / count

# Your UndergroundSystem object will be instantiated and called as such:
# obj = UndergroundSystem()
# obj.checkIn(id,stationName,t)
# obj.checkOut(id,stationName,t)
# param_3 = obj.getAverageTime(startStation,endStation)