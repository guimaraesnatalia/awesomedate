class Date:
    def __init__(self, place, perfect_wether, costs):
        self.place = place
        self.perfect_wether = perfect_wether
        self.costs = costs

    def setPlace(self, place):
        self.place = place

    def setPerfetWether(self, perfect_wether):
        self.perfect_wether = perfect_wether

    def setCosts(self, costs):
        self.costs = costs

    def getPlace(self):
        return self.place

