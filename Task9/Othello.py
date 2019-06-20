class Othello :
    def __init__(self):
        self.board = [['-' for i in range (8)]for j in range(8)]
        self.board[4][4] ,self.board[5][5] = 'W' ,'W'
        self.board[4][5] ,self.board[5][4] = 'B','B' 
        self.player = True
        self.BLACK = True
        self.WHITE = False
        self.CURRENT_PLAYER = {self.BLACK : 'B' , self.WHITE : 'W'}
        self.legal_move = []

    def BalckAndWhiteCount(self):
        black, white = 0, 0
        for row in self.board :
            for cell in row :
                if cell == 'B' :
                    black += 1
                elif cell == 'W':
                    white += 1
        return black,white

    def legal_moves(self,player):
        self.legal_move = []
        row = 0
        for row in range(len(self.board)) :
            for col in range(len(self.board)):
                if self.isLegal(row,col):
                    self.legal_move.append(row,col)
            
        return self.legal_move

    def isLegal(self,row,column):
        check = self.CURRENT_PLAYER.get(self.player)
        for i in range(len(self.board)):
            if(self.board[row][i]==1):
                break
        for i in range(len(self.board)):
            if(self.board[i][column]==1):
                return False
        for i,j in zip(range(row,-1,-1),range(column,-1,-1)):
            if(self.board[i][j]==1):
                return False
        for i,j in zip(range(row,-1,-1),range(column,len(self.board))):
            if(self.board[i][j]==1):
                return False
        return True
            
        
    def displayBoard(self):
        for row in self.board :
            for cell in row :
                print(cell,end = "")
            print()

    def play(self):
        while True :
            black, white = self.BalckAndWhiteCount()
            self.displayBoard()
            print("Blacks :",black," Whites :",white)
            self.legal_move = self.legal_moves(self.CURRENT_PLAYER.get(self.player))
            if len(self.legal_move == 0):
                self.legal_move = self.legal_moves(self.CURRENT_PLAYER.get(not self.player))
                if len(self.legal_move == 0):
                    break    
            print(self.legal_move)
            print("The player is ",self.CURRENT_PLAYER.get(self.player))
            cell = list(map(int,input().split()))
            if cell in self.legal_move  :
                self.board[cell[0]][cell[1]] = self.CURRENT_PLAYER.get(self.player)
            else :
                print ("Sorry not a legal move you missed your chance")
            self.player = not self.player
            

GAME = True
while GAME :
    Othello().play()
    print("\n\nDo you want to Continue(y/n)?")
    choice = input()
    if(choice.lower() != 'y'):
        break