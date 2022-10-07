#Weather
#Developer: Mr. Lange
#Version 1.0

"""
Create a function for our current weather using the
random.choice function to determine what the weather is
picking from a list - using If, elif & Else statements
to check the condition and print a specific print line
"""

#Import Libraries here
import random

#Weather condition list using the random.choice library
#to randomly choose a condition and storing it in its brain
def weather():
    weatherForcast = ["Rain","Snow","Sunny","Cloudy","Foggy","Storming","Icy"]
    weatherCondition = random.choice(weatherForcast)
    return weatherCondition

weatherAlert = weather()
def vehicleResponseSystem():
    if weatherAlert == "Icy":
        print("\nVRS has changed your Alarm 30 minutes earlier based on the NWS forcast of",weatherAlert)


vehicleResponseSystem()