#Gasoline
#Programmer: Mr. Lange
#Version1.0

"""
Define a function to check our gas gauge and determine how far
we have until we need gasoline based on an if, elif, else
condition
"""

#import library here
import random
from time import sleep

# Gas level function
def gasLevelGauge():
    gasLevelList = ["Empty","Low","Quarter Tank","Half Tank","Three Quarter Tank","Full Tank"]
    currentGasLevel = random.choice(gasLevelList)
    return currentGasLevel

# Variable calling the gasLevelGauge function to store value once
gasLevelIndicator = gasLevelGauge()

def listOfGasStations():
    gasStation = ["Shell","Circle K","Marathon","Speedway","Meijer"]
    gasStationNearby = random.choice(gasStation)
    return gasStationNearby

def gasLevelAlert():
    if gasLevelIndicator == "Empty":
        print("***WARNING YOU ARE ON EMPTY***")
        sleep(1)
        print("Calling Emergency Contact")
    elif gasLevelIndicator == "Low":
        print("***WARNING***")
        sleep(1)
        print("Your gas tank is extremely low, checking Google Maps for the closest gas station")
        sleep(1)
        print("The closest gas station is",listOfGasStations())

gasLevelAlert()



