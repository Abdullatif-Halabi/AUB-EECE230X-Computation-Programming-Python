class AUBFL(object):
    def __init__(self, Teams):
        # check if Teams is a list and elements are strings using assert
        assert isinstance(Teams, list), "Invalid Input!"
        for i in Teams:
            assert isinstance(i, str), "Invalid Input!"

        self.Points = {team: 0 for team in Teams}

    def __str__(self):
        s = ""
        for team, point in self.Points.items():
            s += f"{team}: {point}\n"
        return s

    def play(self, team1, team2, score1, score2):
        # check if team1 and team2 are in self.Points using assert
        assert team1 in self.Points, "Invalid Input!"
        assert team2 in self.Points, "Invalid Input!"
        # check if score1 and score2 are integers using assert
        assert isinstance(score1, int), "Invalid Input!"
        assert isinstance(score2, int), "Invalid Input!"

        if score1 > score2:
            self.Points[team1] += 3
        elif score1 < score2:
            self.Points[team2] += 3
        else:
            self.Points[team1] += 1
            self.Points[team2] += 1

    def add(self, team):
        # check if team is in self.Points using assert
        assert team not in self.Points, "Invalid Input!"

        self.Points[team] = 0

    def winner(self):
        winner_team = ""
        for team, point in self.Points.items():
            if point == max(self.Points.values()):
                if winner_team == "":
                    winner_team = team
                else:
                    return "No Winner"
        return winner_team


# League = AUBFL(["CSE", "CIVE", "PremedStudentSociety"])
# print(League)
# League.play("CSE", "PremedStudentSociety", 3, 2)
# print(League)
# League.add("OSB")
# print(League)
# League.play("CIVE", "OSB", 1, 1)
# print(League)
# League.play("OSB", "CSE", 1, 1)
# print(League)
# print("The winner is  " + League.winner())
