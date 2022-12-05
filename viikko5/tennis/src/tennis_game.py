class TennisGame:
    def __init__(self, player1_name, player2_name):
        self.player1_name = player1_name
        self.player2_name = player2_name
        self.m_score1 = 0
        self.m_score2 = 0
        self.score = ""

    def won_point(self, player_name):
        if player_name == self.player1_name:
            self.m_score1 = self.m_score1 + 1
        else:
            self.m_score2 = self.m_score2 + 1

    def who_is_winner(self):
        self.score = ""
        minus_result = self.m_score1 - self. m_score2

        if minus_result == 1:
            self.score = "Advantage player1"
        elif minus_result == -1:
            self.score = "Advantage player2"
        elif minus_result >= 2:
            self. score = "Win for player1"
        else:
            self.score = "Win for player2"
            
    def what_is_the_game_standing_for_player_one(self):
        self.score = ""
        if self.m_score1 == 0:
            self.score = "Love-All"
        elif self.m_score1 == 1:
            self.score = "Fifteen-All"
        elif self.m_score1 == 2:
            self.score = "Thirty-All"
        elif self.m_score1 == 3:
            self.score = "Forty-All"
        else:
            self.score = "Deuce"

    def what_is_the_game_standing_for_player_two(self):
        self.score = ""
        temp_score = 0
        for i in range(1, 3):
            if i == 1:
                temp_score = self.m_score1
            else:
                self.score = self.score + "-"
                temp_score = self.m_score2

            if temp_score == 0:
                self.score = self.score + "Love"
            elif temp_score == 1:
                self.score = self.score + "Fifteen"
            elif temp_score == 2:
                self.score = self.score + "Thirty"
            elif temp_score == 3:
                self.score = self.score + "Forty"
            


    def get_score(self):

        if self.m_score1 == self.m_score2:
            self.what_is_the_game_standing_for_player_one()
            
        elif self.m_score1 >= 4 or self.m_score2 >= 4:
            self.who_is_winner()

        else:
            self.what_is_the_game_standing_for_player_two()

        return self.score
