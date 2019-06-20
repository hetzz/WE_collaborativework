import random

class Play :
    def __init__(self):
        self.player = [i for i in range(2,15)]
        #self.computer = random.shuffle([i for i in range(2,15)])
        self.computer = [i for i in range(2,15)]
        self.diamonds = [i for i in range(2,15)]
        random.shuffle(self.diamonds)
        self.player_score = 0
        self.computer_score = 0

    def strategyRandom(self):
        return self.computer.pop() , self.diamonds.pop()

    def strategyAdd2(self):
        randomIndex = random.randrange(0, len(self.diamonds))
        diamondCard = self.diamonds[randomIndex]
        return self.computer[(randomIndex + 2) % len(self.computer)] , diamondCard

    def showState(self,playerbid,computerbid,diamond_card):
        print("PlayerCard :",playerbid,"ComputerCard", computerbid,"Diamond :", diamond_card,"PlayerScore :" ,self.player_score,"ComputerScore", self.computer_score)

    def Banker(self, diamond_card , playerbid , computerbid):
        if playerbid == computerbid :
            self.player_score += diamond_card / 2
            self.computer_score += diamond_card / 2
        elif playerbid > computerbid :
            self.player_score += diamond_card
        else :
            self.computer_score += diamond_card
        self.player.remove(playerbid)

    def gamePlay(self):
        for i in range(13) :
            if len(self.diamonds) == 0 :
                print("Game Over")
                break
            playerbid = int(input('Enter card : '))
            computerbid, diamond_card = self.strategyAdd2()
            self.Banker(diamond_card, playerbid, computerbid)
            self.showState(playerbid,computerbid,diamond_card)


GAME =True
while GAME :
    game = Play()
    game.gamePlay()
    print("\n\nDo you want to Continue(y/n)?")
    choice = input()
    if(choice.lower() != 'y'):
        break