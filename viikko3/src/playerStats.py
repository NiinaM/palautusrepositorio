class PlayerStats:
    def __init__(self, reader):
        self.players = reader.get_players()

    def top_scorers_by_nationality(self, nationality):

        top_players = sorted(filter(lambda x: x.nationality == nationality, self.players), key=lambda x: x.count_goals_assists(), reverse=True)

        return top_players