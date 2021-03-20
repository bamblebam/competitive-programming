class UndergroundSystem:

    def __init__(self):
        self.travels = dict()
        self.times = dict()

    def checkIn(self, id: int, stationName: str, t: int) -> None:
        self.travels[id] = [id, stationName, t]
        return

    def checkOut(self, id: int, stationName: str, t: int) -> None:
        checkedin = self.travels[id]
        if f"{checkedin[1]}-{stationName}" in self.times:
            self.times[f"{checkedin[1]}-{stationName}"][0] += t-checkedin[2]
            self.times[f"{checkedin[1]}-{stationName}"][1] += 1
        else:
            self.times[f"{checkedin[1]}-{stationName}"] = [t-checkedin[2], 1]
        return

    def getAverageTime(self, startStation: str, endStation: str) -> float:
        time = self.times[f"{startStation}-{endStation}"]
        return time[0]/time[1]

        # Your UndergroundSystem object will be instantiated and called as such:
        # obj = UndergroundSystem()
        # obj.checkIn(id,stationName,t)
        # obj.checkOut(id,stationName,t)
        # param_3 = obj.getAverageTime(startStation,endStation)
