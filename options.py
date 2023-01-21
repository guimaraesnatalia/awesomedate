class Options:
    def __init__(self):
        self.wether = ''
        self.costs = ''

    def setWether(self, wether):
        self.wether = wether

    def setCosts(self, costs):
        self.costs = costs

    def getWether(self):
        return self.wether

    def getCosts(self):
        return self.costs
