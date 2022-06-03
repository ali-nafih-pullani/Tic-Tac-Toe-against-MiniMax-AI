#Playing board as a class
#Creating a class for the board is not required, all the functions can be defined independantly as well
class Board:
    def __init__(self):
        '''input: None, 
        prints the welcome message, instructions and rules,
        attributes of the class: board_as_list -> shows the board in a list format'''
        board = ['position_holder']
        board.extend(list(" " for x in range(9)))
        self.board_as_list = board
        print("Welcome to the Tic-Tac-Toe")
        print('\n')
        print("You are playing against MiniMax AI player, which is UNBEATABLE! If you make good decision, you can get a draw! Good Luck :)")
        print('\n')
        print("Use your numpad to play ")
        print("1|2|3")
        print("-"*5)
        print("4|5|6")
        print("-"*5)
        print("7|8|9")
        print('\n')
        print("Computer's moves are marked by 'X' and your's by 'O'")
        print("Game starts now!!!")
        
    def print_board(self):
        '''input: None, Ouput: None,
        prints the current layout of the board'''
        print(f"{self.board_as_list[1]}|{self.board_as_list[2]}|{self.board_as_list[3]}")
        print("-"*5)
        print(f"{self.board_as_list[4]}|{self.board_as_list[5]}|{self.board_as_list[6]}")
        print("-"*5)
        print(f"{self.board_as_list[7]}|{self.board_as_list[8]}|{self.board_as_list[9]}")
        
    def is_free(self,num):
        '''input: int(a board position),
        output: Boolean'''
        return self.board_as_list[num]==' '
    
    def end_check(self):
        '''input: None,
        output: Boolean (True('X','O','Draw') or False)'''
        winning_combinations = [(1,2,3),(4,5,6),(7,8,9),(1,4,7),(2,5,8),(3,6,9),(1,5,9),(3,5,7)]
        for x,y,z in winning_combinations:
            if (self.board_as_list[x]==self.board_as_list[y]==self.board_as_list[z]=='X'):
                #print("Player 1 wins!")
                return 'X'
            elif (self.board_as_list[x]==self.board_as_list[y]==self.board_as_list[z]=='O'):
                #print("Player 2 wins!")
                return 'O'
            else:
                pass
        if ' ' not in self.board_as_list:
            #print("Game tied!")
            return 'Draw'
        return False
    
    def add_to_board(self,pos_num,player_mark):
        '''input: str(board position), 
        output: None,
        add player's marker to the input position and print the resulting state of the board'''
        while not self.board_as_list[pos_num]==" ":
            try:
                pos_num = int(input("position is taken, try again! :"))
            except:
                print("Invalid input! Enter a number between 1 and 9 !")
                continue
                
        self.board_as_list[int(pos_num)] = player_mark
        print("\n")
        self.print_board()
        print("\n")
    
    def add(self,pos_num,player_mark):
        '''input: str(board position), 
        output: None,
        add player's marker to the input position without printing the resulting state of the board'''
        self.board_as_list[int(pos_num)] = player_mark
        
    def reset_position(self,position):
        '''input: int(board position), 
        output: None,
        resets the marker in the position'''
        self.board_as_list[position] = ' '
        


#Function for player's input
def player_move(board_object):
    while True:
        try:
            pos_num = int(input("Player, Enter your move: "))
            break
        except:
            print('Invalid input! Enter a number between 1 and 9')
        
    board_object.add_to_board(pos_num,'O')

#Function for AI's move
#Initiates the MiniMax recursion for decision making
def comp_move(board_object):
    print('Computer playing ........')
    print('\n')
    current_max = -10000
    current_move = 0
    
    for i in range(1,10):
        if board_object.is_free(i):
            board_object.add(i,'X')
            cost = minimax(board_object,False)
            board_object.reset_position(i)
            if (cost>current_max):
                current_max = cost
                current_move = i
            
    board_object.add(current_move,'X')
    board_object.print_board()





#Minimax AI as a recursive function
def minimax(board,isMaximizing):
    isOver = board.end_check()
    if isOver:
        if isOver=='X':
            a = 1
        elif isOver=='O':
            a = -1
        else:
            a = 0
        if ' ' in board.board_as_list:
            b = board.board_as_list.count(' ') + 1
        else:
            b = 1
        return a*b
    if isMaximizing:
        current_max = -10000
        for i in range(1,10):
            if board.is_free(i):
                board.add(i,'X')
                cost = minimax(board,False)
                board.reset_position(i)
                current_max = max(current_max,cost)
        return current_max
    
    else:
        current_min = 10000
        for i in range(1,10):
            if board.is_free(i):
                board.add(i,'O')
                cost = minimax(board,True)
                board.reset_position(i)
                #pdb.set_trace()
                current_min = min(current_min,cost)
        return current_min




#Game Logic
game_on = True
while game_on:
    print('\n')
    print('-'*20)
    playing_board = Board()
    while True:
        end = playing_board.end_check()
        if end:
            if end=='X':
                print('\n')
                print("Computer wins!")
            elif end=='X':
                print('\n')
                print("Player wins!")
            else:
                print('\n')
                print("Game tied")
            print("\nFinal board: \n")
            playing_board.print_board()
            break
        
        print("\n")
        comp_move(playing_board)
        end = playing_board.end_check()
        if end:
            if end=='X':
                print('\n')
                print("Computer wins!")
            elif end=='X':
                print('\n')
                print("Player wins!")
            else:
                print('\n')
                print("Game tied")
            print("\nFinal board: \n")
            playing_board.print_board()
            break
        print("\n")
        player_move(playing_board)
    print("\n")
    game_on = (input("play again? (Enter 'y' for yes!)").lower() == 'y')
