# File: DataLog.py
# Description: DataLog class file
# Author: F. Eduard Decu
# Date: Mar 2019
# Updated: May 2019

# Imports
# Consts
# Globals
# Functions

#Classes
class DataLog:
    # Updated on May-2019 -> added staff_code
    def __init__(self, id, start_date, end_date,start_time,end_time,access_period,highest_temp, lowest_dp,average_humidity,sensor_readings, staff_code):
        """
        __id: id for this data log, as integer, property with read-only access
        __start_date: start date for this data log,as string, property with read-only access
        __end_date: end date for this data log,as string, property with read-only access
        __start_time: start time for this data log, as string, property with read-only access
        __end_time: end time for this data log, as string, property with read-only access
        __access_period: access period for this data log, as float, property with read-only access
        __highest_temp: highest temperature for this data log, as float, property with read-only access
        __avergae_humidity: average humidity for this data log, as float, property with read-only access
        __sensor_readings: sensor readings for this data log, as list, property with read-only access
        __staff_code: the staff member code for this data log, as a string, property with read-only access

        :param id: to associate with this id data instance
        :param start_date: to associate with this start_date data instance
        :param end_date: to associate with this end_date data instance
        :param start_time: to associate with this start_date data instance
        :param end_time: to associate with this end_time data instance
        :param access_period: to associate with this access_period data instance
        :param highest_temp: to associate with this highest_temp data instance
        :param average_humidity: to associate with this average_humidity data instance
        :param sensor_readings: to associate with this sensor_readings data instance
        :param staff_code: to associate with this staff_code data instance
        """
        self.__id = id
        self.__start_date = start_date
        self.__end_date = end_date
        self.__start_time = start_time
        self.__end_time = end_time
        self.__access_period = access_period
        self.__highest_Temp = highest_temp
        self.__average_Humidity = average_humidity
        self.__sensorReadings = sensor_readings
        self.__staff_code = staff_code # Added on May-2019
        self.__lowest_dp = lowest_dp # Added on May-2019


    @property
    def id(self):
        return self.__id

    @property
    def dataPoints(self):
        return self.__dataPoints




    def Print_data_log(self):
        """
            user friendly representation of this data log
        """

        print("---------------->LOG "+str(self.id)+"<----------------")
        print("Staff member code: {0}".format(self.__staff_code))
        print("ENTER -> Date: {0} Time: {1}".format(self.__start_date, self.__start_time))
        print("EXIT  -> Date: {0} Time: {1}".format(self.__end_date, self.__end_time))
        print("Access period lasted: {0} second(s)".format(self.__access_period))
        print("Highest temperature:  {0:.2f}C".format(self.__highest_Temp))
        print("Lowest dew point temp:     {0:.2f}C".format(self.__lowest_dp)) # added on May-2019
        print("Time stamp | Temperature | Humidity | Dew Point Temp") # dew Point temp added on May-2019
        for values in self.__sensorReadings: #print all the sensor readings values # new value added on May-2019 -> dew point for each sensor readings
            print(values)
        print("---------------------------------------")
        print("")








