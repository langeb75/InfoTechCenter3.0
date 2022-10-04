#Welcome Screen
#Developer: Mr. Lange
#Version: 1.0

"""
Our Welcome Screen will start our program letting
drivers know that the InfoTechCenter OS is Loading
"""

#Import Libraries Here
from time import sleep #We imported the Sleep function from the Time library

import colorama #Changing the color of my text
from colorama import Fore, Back, Style
colorama.init(strip=False, autoreset=True)

print(Fore.RED + "\n\nWelcome to Operation Fury InfoTech Center")
sleep(2)
print("\033[1;36m \nOperation Fury's Operation System Booting Up")