points = {}

def decideMatch(Match_str):
    no_of_gamesA , no_of_gamesB = 0,0
    A,B = 0,0
    for i in Match_str :
        if(i == "A"):
            A += 1
        else :
            B += 1
        if(A >= 5 or B >= 5 and abs(A - B) >= 2):
                
            if(points[str(A) + str(B)] == "Game") :
                no_of_gamesA , no_of_gamesB = check_increment_games(str(A) + str(B),no_of_gamesA , no_of_gamesB)
                A , B = 0,0

            else :


