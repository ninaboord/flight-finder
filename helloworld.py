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



"""

NEWEST:

(function that reads csv and inputs into a dataset)

flightpaths = []

main function(start, end, start date, maxhours, godDict):

    for each flight in godDict that begins in ORIGINAL STARTING AIRPORT and STARTS ON START DATE:
        arrayOfAllPossibleFlightCombos.append(call recursive function)

recursive function(start, final_destination, maxhours, godDict, flightpath):
    if (start == final_destination)
        flightpaths.append(flightpath)
        return
    else:                                                        #what if we chose this flight?
        current time = flight_end_time
         for each flight that begins at flight end:
            if maxhours - traveltime > 0 && current time + 45 < flight_start_time:
                start = flight_end
                recursive_function(start, final_destination, maxhours - traveltime, 
, godDict, flightpath + flight)
    return result



NEW:

(function that reads csv and inputs into a dataset)

main function(start, end, start date, maxhours, godDict):

    for each flight in godDict that begins in ORIGINAL STARTING AIRPORT and STARTS ON START DATE:
        arrayOfAllPossibleFlightCombos.append(call recursive function)

recursive function(start, final_destination, maxhours, godDict, flightpath):
    if (start == final_destination)
        return flightpath
    else:                                                        #what if we chose this flight?
        create empty list called result
        current time = flight_end_time
        for each flight that begins at flight end:
            if maxhours - traveltime > 0 && current time + 45 < flight_start_time:
                start = flight end
                result += recursive_function(start, final_destination, maxhours - traveltime, 
, godDict, flightpath + flight)
    return result
        

(function that sorts flightlist array by price)




OLD:

main  function(start, end, start date, maxhours, godDict):

    for each flight that begins in ORIGINAL STARTING AIRPORT:
        arrayOfAllPossibleFlightCombos.append(call recursive function)

recursive function(start, final_destination, start date, maxhours, 
, godDict, soFar):
    if (flight is a one-way from start to final_destination):
        add flight to flightpath
        return list of flightpaths

    else:
        add current flight to flight path
        for each flight that begins at start:
            if maxhours - traveltime > 0 && flight_start_time + 45 min < SOMETHING:
                add flight to flightpath
                start = flight end
                recursive_function(start, final_destination, start date, maxhours - traveltime, 
, godDict, soFar)
    return "no flights"
        

function that sorts flightlist array by price




        

(function that sorts flightlist array by price)


def createDict():
    godDict = defaultdict()
    reader = csv.DictReader(open('Flights Data Set.csv'))
    for row in reader:
        currflight = Flight(row['Start'], row['End'], row['Depart Date'], row['Depart Time'], row['Arrival Date'], row['Arrival Time'], row['Length'], row['Number'], row['Cost'])
    print(godDict)

    for row in reader:
       godDict.update({row['Start']: {row['end']: {}}})
    

new_data_dict = {}
with open("input.csv", 'r') as data_file:
    data_file.next()
    for row in data_file:
        row = row.strip().split(",")
        new_data_dict.setdefault(row[0],{})[row[1]] = int(row[2])


    print(godDict)



    

"""

