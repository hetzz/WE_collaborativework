import random

class Play :
    def __init__(self):
        self.player = [i for i in range(2,15)]
        self.computer = [i for i in range(2,15)]
        self.diamonds = [i for i in range(2,15)]
        random.shuffle(self.diamonds)
        self.player_score = 0
        self.computer_score = 0

    def strategyRandom(self):
        return self.computer.pop()

    def strategyAdd2(self):
        randomIndex = random.randrange(0, len(self.diamonds))
        diamondCard = self.diamonds[randomIndex]
        return self.computer[(randomIndex + 2) % len(self.computer)] , diamondCard

    def gamePlay(self):
        random.shuffle(self.computer)
        for i in range(13) :
            if len(self.diamonds) == 0 :
                print("Game Over")
                break
            computerbid = self.computer.pop()
            diamond_card = self.diamonds.pop()
            playerbid = int(input('Enter card : '))
            computerbid, diamond_card = self.strategyAdd2()
            print('Computer : ',computerbid ,'\t',playerbid, '\t', diamond_card)
            self.Banker(diamond_card, playerbid, computerbid)
            print("Score :" , self.computer_score, self.player_score)

    def showState(self):
        print(self.player, self.computer, self.diamonds, self.player_score, self.computer_score)

    def Banker(self, diamond_card , playerbid , computerbid):
        if playerbid == computerbid :
            self.player_score += diamond_card / 2
            self.computer_score += diamond_card / 2
        elif playerbid > computerbid :
            self.player_score += diamond_card
        else :
            self.computer_score += diamond_card
        self.player.remove(playerbid)

game = Play()
game.gamePlay()
