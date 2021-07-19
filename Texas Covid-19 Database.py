# File: Project3.py
# Student: Mohammed Jalil
# UT EID: mhj476
# Course Name: CS303E
# 
# Date Created: 5-1-21
# Date Last Modified: 5-3-21
# Description of Program: This program is able to read a Covid county data text file 
# through querying it, will be able to tell you the counties involved, the # of cases in
# a specific county or all of Texas, the # of deaths in a specific county or all of Texas.

import os.path

countyNames = []
totalConfirmedCases = []
totalDeaths = []
nameCasesDeaths = {}
listOfCommands = ['help','quit','counties','cases','deaths']


def welcomeMessage():
    print("")
    print("Welcome to the Texas Covid Database Dashboard.")
    print("This provides Covid data in Texas as of 1/26/21.")
    print("Creating dictionary from file: county-covid-data.txt" )

def helpMessage():
    print("""
Enter any of the following commands:
\033[1mHelp\033[0m - list any available commands;
\033[1mQuit\033[0m - exit this dashboard;  
\033[1mCounties\033[0m - list all Texas counties; 
\033[1mCases <countyName>/Texas\033[0m - confirmed Covid cases in specified county or statewide; 
\033[1mDeaths <countyName>/Texas\033[0m - Covid deaths in specified county or statewide.
""", sep="")

def commandCall():
    commands = input("\033[1mPlease enter a command:\033[0m ")
    handle(commands.lower())

def getNameCasesDeaths():
    with open("county-covid-data.txt", "r") as covidData:
        covidData = covidData.read().splitlines()
        for line in covidData:
            if '#' in line:
                continue
            else:
                line = line.split(',')
                nameCasesDeaths[line[0]]= line[1:]

def getTotalConfirmedCases(): #For all counties
    totalConfirmedCases = 0
    with open("county-covid-data.txt", "r") as covidData:
        covidData = covidData.read().splitlines()
        for line in covidData:
            if '#' in line:
                continue
            else:
                line = line.split(',')
                totalConfirmedCases += int(line[1])
        return totalConfirmedCases

def getTotalDeath(): #For all counties
    totalDeaths = 0
    with open("county-covid-data.txt", "r") as covidData:
        covidData = covidData.read().splitlines()
        for line in covidData:
            if '#' in line:
                continue
            else:
                line = line.split(',')
                totalDeaths += int(line[3])
        return totalDeaths

def getCountiesList(): #List of counties
    with open("county-covid-data.txt", "r") as covidData:
        covidData = covidData.read().splitlines()
        for line in covidData:
            if '#' in line:
                continue
            else:
                line = line.split(',')
                countyNames.append((line[0]))

def HandleHelpCommand():
    print("""\033[1mHelp\033[0m - list any available commands;
\033[1mQuit\033[0m - exit this dashboard; 
\033[1mCounties\033[0m - list all Texas counties; 
\033[1mCases <countyName>/Texas\033[0m - confirmed Covid cases in specified county or statewide; 
\033[1mDeaths <countyName>/Texas\033[0m - Covid deaths in specified county or statewide.
""")
    commandCall()

def HandleQuitCommand():
    print("Thank you for using the Texas Covid Database Dashboard.  Goodbye!")
    print("")
    quit()

def HandleCountiesCommand():
    getCountiesList()
    perLine = 0
    for county in countyNames:
        print(county, end=", ")
        perLine += 1
        if perLine == 10:
            print()
            perLine = 0
    print("")
    print("")
    commandCall()

def HandleCasesCommand(countyName):
    if countyName.lower() == "texas":
        print("Texas total confirmed Covid cases:", getTotalConfirmedCases())
        print("")
        commandCall()
    with open("county-covid-data.txt", "r") as covidData:
        found = False
        covidData = covidData.read().splitlines()
        for line in covidData:
            if '#' in line:
                continue
            else:
                line = line.split(',')
                if line[0].lower() == countyName.lower():
                    found = True
                    print(countyName.title(), "county has", line[1], "confirmed Covid cases.")
                    print("")
    if not found:
        print("County", countyName.title(), "is not recognized.")
        print("")           
    commandCall()

def HandleDeathsCommand(countyName):
    if countyName.lower() == "texas":
        print("Texas total confirmed Covid deaths:", getTotalDeath())
        print("")
        commandCall()
    with open("county-covid-data.txt", "r") as covidData:
        found = False
        covidData = covidData.read().splitlines()
        for line in covidData:
            if '#' in line:
                continue
            else:
                line = line.split(',')
                if line[0].lower() == countyName.lower():
                    found = True
                    print(countyName.title(), "county has", line[3], "fatalities.")
                    print("")
        if not found:
            print("County", countyName.title(), "is not recognized.")
            print("")
    commandCall()


def handle(com):
    commWords = com.split() #splits into list
    word = commWords[0] #gets the first item in the list

    args = commWords[1:] #extract the rest of the words and re-assemble them into a single string 
    arg = " ".join(args) #joined together separated by spaces. 

    if word not in listOfCommands:
        print('Command is not recognized.  Try again!')
        print("")
        commands = input("\033[1mPlease enter a command:\033[0m ")
        handle(commands)
    else:
        #START HANDLE THE COMMAND
        if word == "help":
           HandleHelpCommand()
        elif word == "quit":
            HandleQuitCommand()
        elif word == "counties":
            HandleCountiesCommand()
        elif word == "cases":
            HandleCasesCommand(arg)
        elif word == "deaths":
            HandleDeathsCommand(arg)
        

if os.path.isfile("county-covid-data.txt") is False:
    print("File county-covid-data.txt not found.")
else:
    welcomeMessage()
    helpMessage()
    commandCall()
