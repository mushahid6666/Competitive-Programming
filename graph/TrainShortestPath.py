# class Solution:
class Station:
    name = None
    neighbours = None
    def __init__(self, name):
        self.name = name
        self.neighbours = list()

    def get_name(self):
        return self.name

    def add_neighbour(self, v):
        self.neighbours.append(v)

    def get_neighbours(self):
        return self.neighbours

    def __eq__(self, other):
        """
        :param other: Station
        :return:
        """
        other if self.name == other.get_name()

class TrainMap:
    stations = None
    def __init__(self):
        self.stations = dict()

    def addStation(self, name):
        s = Station(name)
        if name not in self.stations:
            self.stations[name] = s
        return self

    def getStation(self, name):
        return self.stations[name]

    def connectStations(self, fromstation, tostation):