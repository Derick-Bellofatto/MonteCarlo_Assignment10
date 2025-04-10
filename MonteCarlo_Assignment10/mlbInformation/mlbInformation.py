# File Name : mlbInformation.py
# Student Name: Derick, David, Michael, and Nikki
# email:  Bellofdk@mail.uc.edu  Beckerd8@mail.uc.edu    Slivinmb@mail.uc.edu    Carfornc@mail.uc.edu
# Assignment Number: Assignment 10
# Due Date:   4/10/2025
# Course #/Section:   IS4010-001
# Semester/Year:   Spring 2025
# Brief Description of the assignment:  Using an API in order to retrieve real time MLB JSON files and query/interpret data into a CSV file

# Brief Description of what this module does: 

# Anything else that's relevant:

class EventProcessor:
    def __init__(self, events):
        self.events = events

    def display_scores(self):
        for event in self.events:
            competitions = event.get('competitions', [])
            date = event.get('date', 'Unknown Date')
            print("-------------------------------------------------\n")
            print(f"Game: {event.get('shortName', 'Unknown Game')}")
            print(f"Date: {date}\n")


            for competition in competitions:
                competitors = competition.get('competitors', [])
                if 'attendance' in competition:
                        print("Attendance :", competition['attendance'])

                for competitor in competitors:
                    team_name = competitor['team'].get('displayName', 'Unknown Team')
                    score = competitor.get('score', '0')
                    print(f"{team_name}: {score}\n")


                    