# File Name : csv.py
# Student Name: Derick, David, Michael, and Nikki
# email:  Bellofdk@mail.uc.edu  Beckerd8@mail.uc.edu    Slivinmb@mail.uc.edu    Carfornc@mail.uc.edu
# Assignment Number: Assignment 10
# Due Date:   4/10/2025
# Course #/Section:   IS4010-001
# Semester/Year:   Spring 2025
# Brief Description of the assignment:  Using an API in order to retrieve real time MLB JSON files and query/interpret data into a CSV file

# Brief Description of what this module does: 

# Anything else that's relevant:
from mlbInformation.mlbInformation import *

import csv

class CsvProcessor:
    '''
    Retrieves information from the API and puts it into a csv file.
    '''
    def __init__(self, json_data):
        '''
        Initializes CsvProcessor
        '''
        self.json_data = json_data

    def writecsv(self):
        '''
        Retreives data from API and submits it into a csv file with Game, Date, Attendance, Team, and Score colummns. CSV file is then saved in project folder.
        '''
        ourdata =[]
        csvheader =['Game','Date','Attendance','Team','Score']
        for event in self.json_data:
            short_name = event.get('shortName', 'Unkown Game')
            date = event.get('date', 'Unknown Date')

            competitions = event.get('competitions', [])
            for competition in competitions:
                competitors = competition.get('competitors', [])
                attendance = competition.get('attendance','0')
            for competitor in competitors:
                team_name = competitor['team'].get('displayName', 'Unknown Team')
                score = competitor.get('score', '0')
                listing =[short_name, date, attendance,team_name, score]
                ourdata.append(listing)
            


        with open('MLB.csv','w',encoding='UTF8',newline='') as f:
            writer = csv.writer(f)
            writer.writerow(csvheader)
            writer.writerows(ourdata)






