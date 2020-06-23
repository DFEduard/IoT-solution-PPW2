# File: Humidity.py
# Description: Humidity class file
# Author: F. Eduard Decu
# Date: Mar 2019

# Imports
from Sensor import Sensor

# Consts
# Globals
# Functions

#Classes
class Humidity(Sensor):
    """
    Class that hold humidity data as a single data point, inherits from the Sensor class
    to inclued the properties from this class
    """
    def __init__(self, humidity, scale):
        """
        Initialiser- instance variable:

        __value: from Sensor class
        __scale: from Sensor class

        :param humidity: to associate with this humidity data instance
        :param scale: to associate with this scale data instance
        """

        #Using the Sensor class initialiser
        Sensor.__init__(self,humidity,scale)


