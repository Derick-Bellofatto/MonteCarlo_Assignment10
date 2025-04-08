# File Name : main.py
# Student Name: Derick, David, Michael, and Nikki
# email:  Bellofdk@mail.uc.edu  Beckerd8@mail.uc.edu    Slivinmb@mail.uc.edu    Carfornc@mail.uc.edu
# Assignment Number: Assignment 10
# Due Date:   4/10/2025
# Course #/Section:   IS4010-001
# Semester/Year:   Spring 2025
# Brief Description of the assignment:  Using an API in order to retrieve real time MLB JSON files and query/interpret data into a CSV file

# Brief Description of what this module does: This module retrieves MLB JSON data and parses it into a python dictionary as well as calls/executes groupmembers modules
# Citations: Inclass Python API Example, Postman, MLB API

# Anything else that's relevant:

from mlbInformation.mlbInformation import *
from csv.csv import *
import requests
import json


if __name__ == "__main__":
    response = requests.get('https://site.api.espn.com/apis/site/v2/sports/baseball/mlb/scoreboard') #reaches out to MLB's API endpoint and returns current MLB data as "response"
    json_string = response.content #Saves the content to a single string
    parsed_json = json.loads(json_string) # Python dictionary parsed from string
   
    events = parsed_json.get('events', [])
    EventProcessor(events).display_scores()
   # AttendanceDisplay(events).display_attendance()
    
