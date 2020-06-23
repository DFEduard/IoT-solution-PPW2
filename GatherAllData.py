# File: GatherAllData.py
# Description: GatherAllData class file
# Author: F. Eduard Decu
# Date: Mar 2019
# Updated: May 2019

# Imports

from datetime import datetime
from Temperature import Temperature
from Humidity import Humidity
from DataPoint import DataPoint
from DataLog import DataLog

# Consts
# Globals
# Functions

# Classes
class GatherAllData:
    """
    Class info:
    - read a CSV data file based in the attribute given which is tht CSV file path
    - gather all the data from the CSV data file
    - prints the data in a specific format to be easy readable
    """
    def __init__(self, filePath):
        """
        Initialiser - instance variable:

        :param filePath: to associate with this data set instance
        """

        self.__filePath = filePath #File path given when the class is instantiated
        self.__dataPointsList = [] # A list where all data points are saved
        self.__dataLogList = [] # A list with data logs which contain a number of data points for a period of time
        self.read_file() # This method will read the file when the class is initialised

    # Get property
    @property
    def filePath(self):
        return self.__filePath

    # Get property
    @property
    def dataPointsList(self):
        return self.__dataPointsList
    # Get property
    @property
    def dataLogList(self):
        return self.__dataLogList


    def read_file(self):
        """
        This method will read the CSV data file and assign to the data points property a list of the data points held in
        this CSV data file

        :return: nothing
        """

        # Clear down any existing entries
        self.__dataPointsList = []
        self.__dataLogList = []

        # Used as flag to skip the first row from the CSV file which is header
        skip_header_row = False

        # Open the CSV data file for reading and read each text line in sequence until and of life
        file = open(self.filePath,"r")

        # Read each line from the CSV data file
        for line in file:

            # Check to see if the first row has been read
            if skip_header_row:

                # The values of the current row will be splited and save as a tuple
                # each value can be access by it's index
                # the number of indexes will be determined by how many columns are in the CSV data file
                row = line.split(",")

                # Store the values of the current row
                entriNo = str(row[0])
                date = str(row[1])
                timeStamp = str(row[2])
                temperature = str(row[3])
                humidity = str(row[4])
                staff_code = str(row[5]) # Added on May-2019

                # take the date and time values in order to create a datetime object
                splitDateValue = date.split("/") # format: number les then 10 ---> 5/3/2019 || bigger then 10 --> 10/10/2019
                splitTimeValue = timeStamp.split(":") #format: if the numbers are les then 10 ---> 9:1:1 if bigger --->> 11:11:11



                # this datetime object is used to get the 0 in front of the numbers that are les then 10
                date_time_object = datetime(int(splitDateValue[2]),int(splitDateValue[1]),int(splitDateValue[0]),int(splitTimeValue[0]),int(splitTimeValue[1]),int(splitTimeValue[2]))


                timeStamp = date_time_object.time() #time stamp format: less then 10 --> 01:01:00 || bigger then 10 --> 10:20:30


                scaleTemp = "C" # temperature measuring scale
                scaleHumidity = "%" # humidity measuring scale


                tempData = Temperature(float(temperature), scaleTemp) #Create a temperature object and pass the necessary attributes
                humidityData = Humidity(float(humidity), scaleHumidity) #Create a humidity object and pass the necessary attributes

                #Create a datapoint object and pass the necessary attributes
                data_point = DataPoint(entriNo, str(date), str(timeStamp), tempData.value, humidityData.value, staff_code)

                #Add the data point created into a list with data points
                self.dataPointsList.append(data_point.List_format())
            else:
                #When is set to True the data from the CSV file will be read
                skip_header_row = True



    def Print_dataLog(self):

        entry_number = 0 # Used to check for a new log
        counter = 0 # Count how many rows a log has
        highestTemp = 0 # Save the highest temperature from a log
        humidity_total = 0 # Each humidity value will be added and the total will be used to calculate the average
        no_of_read_logs = 0 # Check how many logs have been read
        no_of_printed_logs = 0 # Check how many logs have been printed
        id = 1 # Id for a log
        one_time = True # Used as flag in order to read the first values of a data points list
        startDate = None # First date from a log
        startTime = None # First time stamp from a log
        endDate = None # Last date from a log
        endTime = None # Last time stamp from a log
        sensors_readings = [] # A list that is used to save all the sensor readings for a period of time
        calc_dewpoint = 0 # Save the dew point of a log
        lowest_dewpoint = 0 # Save the lowest dew point from a log
        staff_member_code = 'None' # Save the staff member code
        """
        dataPointList format
        index 0 = [entrie number,date,time stamp,temperature, humidity, staff member code]
        index 1 = [entrie number2,date2,time stamp2,temperature2, humidity2, staff member code2]
        
        For loop is used to take the values of each line in order to check, create and print a data log      
        
        """
        #Read the data from the data points list
        for data in self.dataPointsList:

            # When the entri_number is bigger it means that a new access period is read from the CSV file
            if int(entry_number) <= int(data[0]):
                counter += 1 # count the number of entries from a access period
                humidity_total += data[4] # add the humidity value and store the total
                endDate = str(data[1]) # the last value stored from an access period will be the end date
                endTime = str(data[2]) # the last value stored from an access period  will be the end time

                # is statement to be run only one time
                if one_time:
                    startDate = str(data[1]) # the first value from an access period will be the start date
                    startTime = str(data[2]) # the first value from an access period will be the start time
                    no_of_read_logs +=1 # store the number of logs created
                    one_time = False # flag set to false in order to store the values needed only for one time
                    staff_member_code = data[5]
                    #Added on May-2019
                    lowest_dewpoint = self.calculate_dewPoint(data[3],data[4]) # Save the first dew point temperature

                # Added on May-2019
                calc_dewpoint = self.calculate_dewPoint(data[3],data[4]) # Calculate the dew point temp for each sensor reading


                # save the lowest dew point
                if lowest_dewpoint > calc_dewpoint:  # Added on May-2019
                    lowest_dewpoint = calc_dewpoint # store the lowest dew point

                # check for the highest temperature
                if highestTemp < data[3]:
                    highestTemp = data[3] # store the new highest temperature

                # a list whit all the sensor readings for an access period
                # sensors_readings.append(str(data[2]) +"       "+ str(data[3]) +"C        "+ str(data[4])+"%      "+ str(calc_dewpoint))
                sensors_readings.append("{0}       {1}C       {2}%       {3:.2f}C".format(data[2], data[3], data[4],
                                                                                          calc_dewpoint))
                entry_number = data[0] # store the new entry number
            else:
                average_humidity = humidity_total / counter # calculate the humidity average

                # calculate the number of seconds the access period lasted
                # e.g (endTime[6] + endTime[7]) represents the seconds from a string timestamp, format: 00:00:50
                # e.g accessPeriodLasted = int(50) - int(20)
                accessPeriodLasted = int(endTime[6] + endTime[7]) - int(startTime[6] + startTime[7])

                #create a data log object # UPDATED ON MAY-2019
                data_log = DataLog(id, startDate, endDate, startTime, endTime, abs(accessPeriodLasted), highestTemp,
                                   lowest_dewpoint, average_humidity, sensors_readings, staff_member_code)

                #print the datalog
                data_log.Print_data_log()

                #clear the sensor readings list, otherway the new data log will have the old values plus the new values
                sensors_readings.clear()

                #Increase the id to be given for next log
                id += 1

                #Count how many logs have been printed
                no_of_printed_logs += 1

                #Reste the flag for the new log
                one_time = True

                #Reset the entry number
                entry_number = 0


        #The last log saved will not be printed from the first proccess
        #This is used to print the last log
        # UPDATED ON MAY-2019 - added staff_member_code
        if no_of_read_logs > no_of_printed_logs:
            average_humidity = humidity_total / counter
            accessPeriodLasted = int(endTime[6] + endTime[7]) - int(startTime[6] + startTime[7])
            data_log = DataLog(id, startDate, endDate, startTime, endTime, abs(accessPeriodLasted), highestTemp,
                               lowest_dewpoint, average_humidity, sensors_readings, staff_member_code)

            data_log.Print_data_log()

    # Added on May-2019
    def calculate_dewPoint(self, t,rh):
        td = t - ((100 - int(rh))/5)
        return td




































