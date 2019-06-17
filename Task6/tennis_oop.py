class Tennis:
    
    points = {"0" : "Love","1" :"15" ,"2" :"30" , "3" : "40" , "33" :"Deuce", "diff" :"Adv"}

    def __init__(self, Match_str):
        self.Match_str = Match_str
        self.games_won_A = 0
        self.games_won_B = 0
        self.sets_A = 0
        self.sets_B = 0
        self.A = 0
        self.B = 0

    def check_increment_sets(self):

    	if (max(self.games_won_A, self.games_won_B) >= 6 and (abs(self.games_won_B - self.games_won_A) >= 2)):
    		if (self.games_won_A > self.games_won_B):
    			return (self.sets_A + 1, self.sets_B)
    		return(self.sets_A, self.sets_B + 1)
    	return (self.sets_A, self.sets_B)

    def check_increment_games(self):
        score_string = str(self.A) + str(self.B)
        if (int(score_string[0]) > int(score_string[1])):
            return (self.games_won_A + 1, self.games_won_B)
        return (self.games_won_A, self.games_won_B + 1)

    def decideMatch(self):
        
        for i in self.Match_str :
            if(i == "A"):
                self.A += 1
            else :
                self.B += 1
            if(abs(self.A - self.B) >= 2 and (self.A >= 4 or self.B >= 4) ):
                self.games_won_A , self.games_won_B = self.check_increment_games()
                self.sets_A, sets_B = self.check_increment_sets()
                self.A , self.B = 0, 0
        
        return (self.A, self.B, self.games_won_A , self.games_won_B, self.sets_A, self.sets_B)

    def printScore(self):
        if (self.A == self.B and self.A < 3) :
            return(self.points[str(self.A)] + " All")

        elif (self.A < 4 and self.B < 4) :
            return(self.points[str(self.A)], self.points[str(self.B)])

        elif(self.A == self.B and self.A >=3):
            return("Deuce")

        elif(self.A != self.B and self.A >=3 and self.B >=3 and self.A - self.B == 1):
            if(self.A > self.B):
                return(self.points["diff"] + " 40")
            else :
                return("40 " + self.points["diff"])

match = Tennis("AABBAABA")
A, B, games_won_A, games_won_B, sets_A, sets_B = match.decideMatch()
print(sets_A, sets_B)
print(games_won_A, games_won_B)
print(match.printScore())