import random
class Play :
    def __init__(self):
        self.player = [i for i in range(2,15)]
        self.computer = [i for i in range(2,15)]
        self.diamonds = [i for i in range(2,15)]
        self.score_player = 0
        self.score_computer = 0

    def generateDiamond_card(self):
	    return self.diamonds[random.randrange(0, len(self.diamonds))]

    def generateComputer_card(self):
		return self.computer[random.randrange(0, len(self.computer))]

    def gamePlay(self):
        for i in range(13) :
            if len(self.diamonds) == 0 :
                print("Game Over")
                break
            computer_card = self.generateComputer_card()
            diamond_card = self.generateDiamond_card()
            player_card = int(input())
            print(computer_card ,'\t',player_card)
            print("Score :" , self.score_computer, self.score_player)
            self.Banker(diamond_card, player_card, computer_card)

    def showState(self):
        print(self.player, self.computer, self.diamonds, self.score_player, self.score_computer)

    def Banker(self, diamond_card , player_card , computer_no):
        if player_card == computer_no :
            self.score_player, self.score_computer = diamond_card / 2, diamond_card / 2
        elif player_card > computer_no :
            self.score_player += diamond_card
        else :
            self.score_computer += diamond_card
        self.diamonds.remove(diamond_card)
        self.player.remove(player_card)
        self.computer.remove(computer_no)

game = Play()
game.gamePlay()
