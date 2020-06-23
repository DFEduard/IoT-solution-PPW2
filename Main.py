# File: Main.py
# Description: Main programme
# Author: F. Eduard Decu
# Date: Mar 2019
# Updated: May 2019

# Imports
from GatherAllData import GatherAllData

# Consts
# Globals
# Functions

# Program entrance function
def main():

    #the CSV data file path
    filePath = "dataLog/data.csv"

    file = GatherAllData(filePath)


    #Prints all the data logs from the file
    file.Print_dataLog()

# Invoke main() program entrance
if __name__ == '__main__':
    main()