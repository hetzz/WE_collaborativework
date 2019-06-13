points = {"0" : "Love","1" :"15" ,"2" :"30" , "3" : "40" , "4" :"Game" , "33" :"Deuce", "diff" :"Adv"}


def check_increment_sets(games_won_A, games_won_B, sets_A, sets_B):

	if (max(games_won_A, games_won_B) >= 6 and (abs(games_won_B - games_won_A) >= 2)):
		if (games_won_A > games_won_B):
			return (sets_A + 1, sets_B)
		else:
			return(sets_A, sets_B + 1)

	return (sets_A, sets_B)

def check_increment_games(score_string, games_won_A, games_won_B):

	if (int(score_string[0]) > int(score_string[1])):
		return (games_won_A + 1, games_won_B)
	return (games_won_A, games_won_B + 1)

def decideMatch(Match_str):
    no_of_gamesA , no_of_gamesB = 0,0
    setsA , setsB = 0,0
    A,B = 0,0
    for i in Match_str :
        if(i == "A"):
            A += 1
        else :
            B += 1
        if(A >= 4 or B >= 4 and abs(A - B) >= 2):
            no_of_gamesA , no_of_gamesB = check_increment_games(str(A) + str(B),no_of_gamesA , no_of_gamesB)
            setsA, setsB = check_increment_sets(no_of_gamesA , no_of_gamesB,setsA , setsB)
            A , B = 0,0
    
    
     
    return (A,B,no_of_gamesA , no_of_gamesB,setsA , setsB)

########################################################################

A, B, no_of_gamesA , no_of_gamesB,setsA , setsB = decideMatch("ABABBBAAB")
   
print(setsA, setsB)
print(no_of_gamesA ,no_of_gamesB)
if (A == B and A != 3) :
    print(points[str(A)] + " All")
elif (A <= 4 and B <= 4) :
    print(points[str(A)],points[str(B)])

        
        


