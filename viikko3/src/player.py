class Player:
    def __init__(self, name, team, goals, assists, nationality):
        self.name = name
        self.team = team
        self.goals = goals
        self.assists = assists
        self.nationality = nationality

    
    def count_goals_assists(self):
        sum_goals_assists = self.goals + self.assists
        return sum_goals_assists
        

    def __str__(self):
        return f"{self.name:20}" + " team: " + str(self.team) + " " + str(self.goals) + " + " + str(self.assists) + " = " + str(self.count_goals_assists())
