import csv
from collections import defaultdict


class Flight:
    def __init__(self, start, end, depart_date, depart_time, arrival_date, arrival_time, length, number, cost):
        self.start = start
        self.end = end
        self.depart_date = depart_date
        self.depart_time = depart_time
        self.arrival_date = arrival_date
        self.arrival_time = arrival_time
        self.length = length
        self.number = number
        self.cost = cost

# these will be user inputted values later
USER_START = 'SFO'
USER_END = 'CDG'
USER_DEPART_DATE = '10/11/24'
USER_MAXHOURS = '24'

# sample dictionary entries 
godDict = {
    'SFO' : {
        'CDG' : [Flight(), Flight()],
        'BRU' : [Flight()]
    },

    'AMS' :  {
        'SFO' : [Flight(), Flight(), Flight()],
        'CDG' : [Flight()],
        'JFK' : [Flight(), Flight(), Flight()]
    }
}

allPossibleFlights = []

def fromLocation(user_start, user_end, user_depart_date, maxHours godDict){
    for loc in godDict[start]: # iterate through possible end locations from starting point in depart date
        flightFinder(user_start, user_end, maxHours, godDict, [])
}

def flightFinder(start, user_end, maxHours, godDict, flightpath):
    if (start == user_end):
        allPossibleFlights.append(flightpath)
        return

    else:
        flightpath = []
        currTime = Flight.arrival_time # this should be the specific flight in start: end part of godDict
        for flight in godDict[start]: # this should be a dict so maybe double for loops here
            if maxHours - Flight.length > 0 and currTime + 45 < Flight.depart_time:
                flightFinder(Flight.end, user_end, maxHours - Flight.length, godDict, flightpath + Flight) # we should also subtract layover time from maxHours
    return flightpath


def main():
    return

if __name__ == "__main__":
    main()


