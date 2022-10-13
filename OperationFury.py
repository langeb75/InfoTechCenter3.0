
#**************************************************************************************
#Import Libraries Here
from time import sleep #We imported the Sleep function from the Time library

import colorama #Changing the color of my text
from colorama import Fore, Back, Style
colorama.init(strip=False, autoreset=True)

import random
#**************************************************************************************


#Welcome Screen
#Developer: Mr. Lange
#Version: 1.0

"""
Our Welcome Screen will start our program letting
drivers know that the InfoTechCenter OS is Loading
"""

print(Fore.RED + "\n\nWelcome to Operation Fury InfoTech Center")
sleep(2)
print("\033[1;36m \nOperation Fury's Operation System Booting Up")

for i in range(2):
    print("OS Booting Up")
    sleep(1)

#*************************************************************************************

#Weather
#Developer: Mr. Lange
#Version 1.0

"""
Create a function for our current weather using the
random.choice function to determine what the weather is
picking from a list - using If, elif & Else statements
to check the condition and print a specific print line
"""

#Weather condition list using the random.choice library
#to randomly choose a condition and storing it in its brain
def weather():
    weatherForcast = ["Rain","Snow","Sunny","Windy","Foggy","Storming","Icy"]
    weatherCondition = random.choice(weatherForcast)
    return weatherCondition

weatherAlert = weather()
def vehicleResponseSystem():
    if weatherAlert == "Icy":
        print("\nVRS has changed your Alarm 30 minutes earlier based on the NWS forcast of",weatherAlert)
        print("VRS will only allow your car to go 30MPH")
    elif weatherAlert == "Snow":
        print("\nVRS has changed your Alarm 15 minutes earlier based on the NWS forcast of", weatherAlert)
        print("VRS will only allow your car to go 50MPH")
    elif weatherAlert == "Rain":
        print("\nVRS has changed your Alarm 5 minutes earlier based on the NWS forcast of", weatherAlert)
        print("VRS will only allow your car to go 60MPH")
    elif weatherAlert == "Windy":
        print("\nVRS has changed your Alarm 5 minutes earlier based on the NWS forcast of", weatherAlert)
        print("VRS will only allow your car to go 70MPH")
    elif weatherAlert == "Foggy":
        print("\nVRS has changed your Alarm 5 minutes earlier based on the NWS forcast of", weatherAlert)
        print("VRS will only allow your car to go 60MPH")
    elif weatherAlert == "Storming":
        print("\nVRS has changed your Alarm 15 minutes earlier based on the NWS forcast of", weatherAlert)
        print("VRS will only allow your car to go 50MPH")
    else:
        print("\nThe weather today is",weatherAlert,"let's Goooo!")
        print("VRS will only allow your car to go 75MPH")


#*************************************************************************************

#Gasoline
#Programmer: Mr. Lange
#Version1.0

"""
Define a function to check our gas gauge and determine how far
we have until we need gasoline based on an if, elif, else
condition
"""

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
    milesToGasStationLow = round(random.uniform(1,25),2)
    milesToGasStationQuarterTank = round(random.uniform(26,50), 2)
    if gasLevelIndicator == "Empty":
        print("***WARNING YOU ARE ON EMPTY***")
        sleep(1)
        print("Calling Emergency Contact")
    elif gasLevelIndicator == "Low":
        print("***WARNING***")
        sleep(1)
        print("Your gas tank is extremely low, checking Google Maps for the closest gas station")
        sleep(1)
        print("The closest gas station is",listOfGasStations(),"which is",milesToGasStationLow,"miles away.")
    elif gasLevelIndicator == "Quarter Tank":
        print("***WARNING***")
        sleep(1)
        print("Your gas tank is a quarter tank full, checking Google Maps for the closest gas station")
        sleep(1)
        print("The closest gas station is",listOfGasStations(),"which is",milesToGasStationQuarterTank,"miles away.")
    elif gasLevelIndicator == "Half Tank":
        print("Your gas tank is a half full, you have plenty of gas to get where you are going")
    elif gasLevelIndicator == "Three Quarter Tank":
        print("Your gas tank is a three quarter full, you have plenty of gas to get where you are going")
    else:
        print("Your gas tank is full, you have plenty of gas to get where you are going")


#*************************************************************************************

#Call Functions Here...

print()
gasLevelAlert()

vehicleResponseSystem()






