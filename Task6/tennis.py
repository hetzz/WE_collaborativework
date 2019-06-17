class Tennis :
    points = {"0" : "Love","1" :"15" ,"2" :"30" , "3" : "40" , "33" :"Deuce", "diff" :"Adv"}

    def __init__(self,Match_str):
        self.Match_str = Match_str
        self.A = 0
        self.B = 0
        self.no_of_gamesB = 0
        self.no_of_gamesA = 0
        self.setsA = 0
        self.setsB = 0
    
    def check_increment_sets(self):

        if (max(self.no_of_gamesA, self.no_of_gamesB) >= 6 and (abs(self.no_of_gamesB - self.no_of_gamesA) >= 2)):
            if (self.no_of_gamesA > self.no_of_gamesB):
                return (self.setsA + 1, self.setsB)
            else:
                return(self.setsA, self.setsB + 1)

        return (self.setsA, self.setsB)

    def check_increment_games(self):
        score_string = str(self.A) + str(self.B)
        if (int(score_string[0]) > int(score_string[1])):
            return (self.no_of_gamesA + 1, self.no_of_gamesB)
        return (self.no_of_gamesA, self.no_of_gamesB + 1)

    def decideMatch(self):
        for i in self.Match_str :
            if(i == "A"):
                self.A += 1
            else :
                self.B += 1
            if(abs(self.A - self.B) >= 2 and (self.A >= 4 or self.B >= 4) ):
                self.no_of_gamesA , self.no_of_gamesB = self.check_increment_games()
                self.setsA, self.setsB = self.check_increment_sets()
                self.A , self.B = 0,0
        
        return (self.A, self.B, self.no_of_gamesA , self.no_of_gamesB, self.setsA , self.setsB)

    ########################################################################
    def printScore(self):
        if (self.A == self.B and self.A < 3) :
            return(self.points[str(self.A)] + " All")

        elif (self.A < 4 and self.B < 4) :
            return(self.points[str(self.A)],self.points[str(self.B)])

        elif(self.A == B and self.A >=3):
            return("Deuce")

        elif(self.A != self.B and self.A >=3 and self.B >=3 and self.A - self.B == 1):
            if(self.A > self.B):
                return(self.points["diff"] + " 40")
            else :
                return("40 " + self.points["diff"])

m = Tennis("AABBAABA")
A, B, no_of_gamesA , no_of_gamesB,setsA , setsB = m.decideMatch()
print(setsA, setsB)
print(no_of_gamesA ,no_of_gamesB)
print(*"".join(m.printScore()))
