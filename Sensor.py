# File: Sensor.py
# Description: Sensor class file
# Author: F. Eduard Decu
# Date: Mar 2019
# Updated: May 2019

# Imports



# Consts

# Globals
# Functions

class Sensor():
    """
    Sensor class for all CSV data file point entities
    """

    def __init__(self, value, scale):
        """
        Initialiser - instance variables:

        __value: sensor value taken
        __scale: measurement unit for the sensor

        :param value: to associate with this data point instance
        :param scale: to associate with this data point instance
        """

        self.__value = value
        self.__scale = scale

    """
    Read-only properties
    """
    @property
    def value(self):
        return self.__value

    @property
    def scale(self):
        return self.__scale


    def __str__(self):
        """
        To string method

        :return: string representation of this class
        """
        s = "{0}{1}".format(self.value, self.scale)
        return s

