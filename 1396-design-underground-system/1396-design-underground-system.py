class UndergroundSystem:

    def __init__(self):
        self.customers = {}
        self.times = {}

    def checkIn(self, id: int, stationName: str, t: int) -> None:
        if id in self.customers:
            return
        
        self.customers[id] = (stationName, t)

    def checkOut(self, id: int, stationName: str, t: int) -> None:
        if id not in self.customers:
            return
        
        in_station = self.customers[id][0]
        in_time = self.customers[id][1]
        time = t - in_time
        
        del self.customers[id]
        
        if (in_station, stationName) in self.times:
            self.times[(in_station, stationName)].append(time)
        else:
            self.times[(in_station, stationName)] = [time]
            

    def getAverageTime(self, startStation: str, endStation: str) -> float:
        if (startStation, endStation) not in self.times:
            return -1
        
        sum = 0
        for time in self.times[(startStation, endStation)]:
            sum += time
        
        return sum / len(self.times[(startStation, endStation)])


# Your UndergroundSystem object will be instantiated and called as such:
# obj = UndergroundSystem()
# obj.checkIn(id,stationName,t)
# obj.checkOut(id,stationName,t)
# param_3 = obj.getAverageTime(startStation,endStation)