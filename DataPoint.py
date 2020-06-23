# File: DataPoint.py
# Description: DataPoint class file
# Author: F. Eduard Decu
# Date: Mar 2019
# Updated: May 2019

# Imports
# Consts
# Globals
# Functions

#Classes
class DataPoint:
    # Updated on May-2019 -> added staff_code
    def __init__(self, entry_no, date,time_stamp, temp_data, humidity_data, staff_code):
        """
        Initialiser - instance variables:

        __time_stamp: time stamp for this data point, as string, preferable format (00:00:00), property with read-only access
        __date: date for this data point, as string, preferable format 11/11/1111, property with read-only access
        __temp_data: temperature data for this data point, as Temperature data instance, property with read-only access
        __humidity_data: humidity data point for this data point, as Humidity data instance, property with read-only access
        __entry_no: used as an identification of this data point, as integer, property with read-only access
        __staff_code: staff member code used to identify the member, as string, property with read-only access (added May-2019)

        :param entry_no: to associate with this data point instance, as int
        :param date: to associate with this data point instance, as date (01/02/2019)
        :param time_stamp: to associate with this data point instance, as string (00:00:00)
        :param temp_data: to associate with this data point instance, as float
        :param humidity_data: to associate with this data point instance, as float
        :param staff_code: to associate with this data point instance, as string (added May-2019)
        """
        self.__time_stamp = time_stamp
        self.__date = date
        self.__temp_data = temp_data
        self.__humidity_data = humidity_data
        self.__entry_no = entry_no
        self.__staff_code = staff_code # Added on May-2019

    """
    Read-only properties 
    """
    @property
    def date(self):
        return self.__date

    @property
    def timeStamp(self):
        return self.__time_stamp

    @property
    def tempData(self):
        return self.__temp_data

    @property
    def humidityData(self):
        return self.__humidity_data

    @property
    def entry_no(self):
        return  self.__entry_no

    #Added on May-2019
    @property
    def staffCode(self):
        return self.__staff_code

    def __str__(self):
        """
        To string method
        :return: string representation of this class
        """
        s = "{0},{1},{2},{3},{4},{5}".format(self.entry_no, self.date, self.timeStamp, self.tempData, self.humidityData, self.staffCode)
        return s

    def List_format(self):
        """
        This method returns a tuple form of all the entries from this data point class
        :return: tuple
        """
        return self.entry_no, self.date,self.timeStamp,self.tempData, self.humidityData, self.staffCode
