def initialise(n1, n2):
	return (0, 0)

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