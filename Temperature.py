# File: Temperature.py
# Description: Temperature class file
# Author: F. Eduard Decu
# Date: Mar 2019
# Updated: May 2019

# Imports
from Sensor import Sensor

# Consts
# Globals
# Functions

#Classes
class Temperature(Sensor):
    """
    Class that hold temperature data as a single data point, inherits from the Sensor class
    """
    def __init__(self, temp, scale):
        """
        __value: from Sensor class
        __scale: from  Sensor class

        :param temp: to associate with this temperature data instance
        :param scale: to associate with this scale data instance
        """

        #Using the Sensor class initialiser
        Sensor.__init__(self,temp,scale)





