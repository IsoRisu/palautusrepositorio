class TennisGame:
    def __init__(self, player1_name, player2_name):
        self.player1_name = player1_name
        self.player2_name = player2_name
        self.m_score1 = 0
        self.m_score2 = 0

    def won_point(self, player_name):
        if player_name == "player1":
            self.m_score1 = self.m_score1 + 1
        else:
            self.m_score2 = self.m_score2 + 1

    def equal_score(self, output):
        if self.m_score1 == 0:
            output = "Love-All"
        elif self.m_score1 == 1:
            output = "Fifteen-All"
        elif self.m_score1 == 2:
            output = "Thirty-All"
        else:
            output = "Deuce"

        return output

    def advantage_and_win(self, output):
        result_difference = self.m_score1 - self. m_score2

        if result_difference == 1:
            output = "Advantage player1"
        elif result_difference == -1:
            output = "Advantage player2"
        elif result_difference >= 2:
            output = "Win for player1"
        else:
            output = "Win for player2"

        return output

    def differnce_in_points(self, output):
        temp_score = 0
        for i in range(1, 3):

            if i == 1:
                temp_score = self.m_score1
            else:
                output += "-"
                temp_score = self.m_score2

            if temp_score == 0:
                output = output + "Love"
            elif temp_score == 1:
                output += "Fifteen"
            elif temp_score == 2:
                output += "Thirty"
            elif temp_score == 3:
                output += "Forty"

        return output


    def get_score(self):
        output = ""

        if self.m_score1 == self.m_score2:
            output = self.equal_score(output)
        elif self.m_score1 >= 4 or self.m_score2 >= 4:
            output = self.advantage_and_win(output)
        else:
            output = self.differnce_in_points(output)

        return output
