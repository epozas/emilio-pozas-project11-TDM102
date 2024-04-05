class Flight:
    def __init__(self, flight_number, origin_ID, dest_ID, dep_time, arr_time, dep_delay,arr_delay):
        self.flight_number = flight_number
        self.origin_ID = origin_ID
        self.dest_ID = dest_ID
        self.dep_time = dep_time
        self.arr_time = arr_time
        self.dep_delay = dep_delay
        self.arr_delay = arr_delay
    
    def get_arrdelay(self):
        return self.arr_delay
    
import pandas as pd
columns_to_read= [
    'DepDelay', 'ArrDelay', 'Flight_Number_Reporting_Airline', 'Distance',
    'CarrierDelay', 'WeatherDelay',
    'DepTime', 'ArrTime', 'Origin',
    'Dest', 'AirTime'
]

col_types = {
    'Flight_Number_Reporting_Airline': 'int64',
    'Origin': 'object',
    'Dest' : 'object',
    'DepTime': 'float64',
    'DepDelay': 'float64',
    'ArrTime': 'float64',
    'ArrDelay': 'float64',
    'Distance': 'float64',
    'CarrierDelay': 'float64',
    'WeatherDelay': 'float64',
}

myDF = pd.read_csv("/anvil/projects/tdm/data/flights/2014.csv", usecols =columns_to_read, dtype=col_types, nrows=100 )
myDF.head()

longlistofflights = []
for index, row in myDF.iterrows():
    myflight = Flight(
        flight_number = row['Flight_Number_Reporting_Airline'],
        origin_ID = row['Origin'],
        dest_ID = row['Dest'],
        dep_time = row['DepTime'],
        arr_time = row['ArrTime'],
        dep_delay = row['DepDelay'],
        arr_delay = row['ArrDelay'],
    )
    longlistofflights.append(myflight)
    

delay_dest = {}
for myflight in longlistofflights:
    if myflight.dest_ID not in delays_dest:
        delays_dest[myflight.dest_ID] = []
    delays_dest[myflight.dest_ID].append(myflight.get_arrdelay())
    
delays_dest

average_delays = {myairport: sum(mydelays)/len(mydelays) for myairport, mydelays in delays_dest.items()}
                  
average_delays

def arr_avg_delays(myflightslist):
    """
    Purpose:To obtain the average arrival delays from each airport ID. 
    Input: myflightslist: List of object Flights
    Output: average_delays: Dictonary with airport : Average delays
    """
    delays_dest = {}
    for myflight in myflightslist:
        if myflight.dest_ID not in delays_dest:
            delays_dest[myflight.dest_ID] = []
        delays_dest[myflight.dest_ID].append(myflight.get_arrdelay())
    average_delays = {myairport: sum(mydelays)/len(mydelays) for myairport, mydelays in delays_dest.items()}
    return average_delays

arr_avg_delays(longlistofflights)

class Flight:
    def __init__(self, flight_number, origin_ID, dest_ID, dep_time, arr_time, dep_delay,arr_delay):
        self.flight_number = flight_number
        self.origin_ID = origin_ID
        self.dest_ID = dest_ID
        self.dep_time = dep_time
        self.arr_time = arr_time
        self.dep_delay = dep_delay
        self.arr_delay = arr_delay
    
    def get_arrdelay(self):
        return self.arr_delay
    
    def get_depdelay(self):
        return self.dep_delay
    
def dep_avg_delays(myflightslist):
    """
    Purpose:To obtain the average arrival delays from each airport ID origin. 
    Input: myflightslist: List of object Flights
    Output: average_delays: Dictonary with airport : Average delays
    """
    delays_origin = {}
    for myflight in myflightslist:
        if myflight.origin_ID not in delays_origin:
            delays_origin[myflight.origin_ID] = []
        delays_origin[myflight.origin_ID].append(myflight.get_depdelay())
    average_delays = {myairport: sum(mydelays)/len(mydelays) for myairport, mydelays in delays_origin.items()}
    return average_delays

dep_avg_delays(longlistofflights)