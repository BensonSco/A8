# Andrew Malone
# Section 003
# This program uses OOP give the season stats on a women's soccer team based on random number generation. The season stats are then shown at the end. 

# Inport Random Library
import random

# Create the class and constructor
class soccerTeam() :
    def __init__(self, teamName) :
        self.team_name = teamName
        self.wins = 0
        self.losses = 0
        self.goals_scored = 0
        self.goals_allowed = 0

# Method seasonStatus with return
    def seasonStatus(self) :
        self.win_loss_pct = self.wins / (self.wins + self.losses)
        if self.win_loss_pct >= .75 :
            self.sSeasonStatus = f"{self.team_name} had a season win/loss percentage of {self.win_loss_pct}. {self.team_name} qualified for the NCAA Women's Soccer Tournament!\n"
        elif self.win_loss_pct >= .50 :
            self.sSeasonStatus = f"{self.team_name} had a season win/loss percentage of {self.win_loss_pct}. {self.team_name} had a good season.\n"
        else :
            self.sSeasonStatus = f"{self.team_name} had a season win/loss percentage of {self.win_loss_pct}. {self.team_name} needs to practice!\n"

        return(self.sSeasonStatus)

# Ask for home team name
sHomeName = input("\nEnter the name of your home soccer team\n").upper()

# Create instance of soccerTeam
oTeam = soccerTeam(sHomeName)

# Ask for number of games to play
bCond = True
while bCond == True :
    try :
        iNumGames = int(input(f"Enter the number of games that {oTeam.team_name} will play\n"))
        bCond = False
    except :
        print("Please insert an integer number for the number of games that will be played")

# Use loop to go through number of game specified
for iCount in range(0,iNumGames) :
    sAwayTeam = input("Enter the name of the away team for game " + str(iCount + 1) + "\n").upper()
    
    bCond = True
    while bCond == True :
        # Generate random scores for each team (have each team have the same range of random scores)
        iHomeScore = random.randint(0, 12)
        iAwayScore = random.randint(0, 12)

        # If there is a tie, regenerate the scores until their isn't a tie 
        if iHomeScore == iAwayScore :
            bCond = True
        else :
            bCond = False

    # Keep track of the season record
    # Use if to start at 0
    if iCount == 0 :
        oTeam.wins = 0
        oTeam.losses = 0

    # Keep track of if the home game won or lost the game based on the scores
    if iHomeScore > iAwayScore :
        oTeam.wins += 1
    else :
        oTeam.losses += 1
    
    # Keep track of the total number of goals scored and total number of goals allowed
    if iCount == 0 :
        oTeam.goals_scored = 0
        oTeam.goals_allowed = 0
            
    oTeam.goals_scored += iHomeScore
    oTeam.goals_allowed += iAwayScore

    # Print out team name and score "BYU's score: 6 UVU's score: 0" for each 
    print("\n" + oTeam.team_name + "'s score: " + str(iHomeScore) + "\n" + sAwayTeam + "'s score: " + str(iAwayScore) + "\n")

# Display Home team name, final season record, total goals scored, total goals allowed, result of seasonStatus method
print(oTeam.team_name)
print(f"Final Season Record: {oTeam.wins} - {oTeam.losses}")
print(f"Total Goals Scored: {oTeam.goals_scored} - Total Goals Allowed: {oTeam.goals_allowed}")
print(oTeam.seasonStatus())