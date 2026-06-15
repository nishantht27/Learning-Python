import random


board = ['1','2','3','4','5','6','7','8','9']
print('Welcome To Tic Tac Toe Game')
print('1.Multiplayer (1V1)')
print('2.Computer')
def print_board():
    
    print()
    print(f'| {board[0]} | {board[1]} | {board[2]} |')
    print(' -- -- -- ')
    print(f'| {board[3]} | {board[4]} | {board[5]} |')
    print(' -- -- -- ')
    print(f'| {board[6]} | {board[7]} | {board[8]} |')
    print()
print_board()

def check_winner():
    wins = [
    [0,1,2],
    [3,4,5],
    [6,7,8],
    [0,3,6],
    [1,4,7],
    [2,5,8],
    [0,4,8],
    [2,4,6]
]
    for a, b, c in wins:
        if board[a] == board[b] == board[c] :
            return board[a]
    return None
    
def check_draw():
    return all(i in ['X','O'] for i in board)
    
def game_status(first_player, second_player):
        winner = check_winner()
        if winner == first_player:
            print('First Player Wins!')
            return True
        elif winner == second_player:
            print('Second Player Wins!')
            return True
            
        if check_draw():
            print('Match was Draw')
            return True
        return False

def computer_status(first_player, computer):
        winner = check_winner()
        if winner == first_player:
            print('First Player Wins!')
            return True
        elif winner == computer:
            print('Computer Wins')
            return True
        
        if check_draw():
            print('Match Was Draw!')
            return True 
        return False
 
def play_again():      
        again = input('Try Again? (yes/no):').lower()
        if again == 'yes':
             board[:] = ['1','2','3','4','5','6','7','8','9']
             print('Welcome To Tic Tac Toe Game')
             print('1.Multiplayer (1V1)')
             print('2.Computer')
             print_board()
             main()
             first_player, second_player = input_choice()
             return True
        elif again == 'no':
             print('Thanks for playing')
             return False
        else :
             print('Enter a Valid option')
             return play_again()
        return False

def input_choice():
    
    first_player = input('First player (X/O) :').upper()
    
    if first_player == 'X':
        print(f'First Player chose : {first_player}')
        second_player = 'O'
        print(f'Second Player chose : {second_player}')
        return first_player, second_player
    elif first_player == 'O':
        print(f'First Player chose : {first_player}')
        second_player = 'X'
        print(f'Second Player chose : {second_player}')
        return first_player, second_player
    else :
        print('Invalid Option')
        return input_choice()
    return False
def main(): 
   
   try:
       choice = int(input('Enter mode (1/2) :'))
   except ValueError :
       print('Enter a valid option')
       exit()
 
   if choice == 1:

       first_player, second_player = input_choice()
        
       while True:
        
           try:    
               first_person = int(input('First player position (1-9): '))
           except ValueError :
               print('Invalid Position')
               continue
        
           if first_person not in range(1,10):
               print('Enter position between 1-9')
               continue
        
           if board[first_person - 1] not in ['X', 'O']:
               board[first_person - 1] = first_player
           else:
               print('Already Filled')
               continue
            
           print_board()
        
           if game_status(first_player, second_player):
               if play_again():
                    continue
               break

           while True:
               try:
                   second_person = int(input('Second player position (1-9): '))
               except ValueError :
                   print('Invalid Position')
                   continue
            
               if second_person not in range(1,10):
                   print('Enter position between 1-9')
                   continue
            
               if board[second_person - 1] not in ['X', 'O']:
                   board[second_person - 1] = second_player
               else:
                   print('Already Filled')
                   continue
                
               print_board()
            
               if game_status(first_player, second_player):
                   if play_again():
                       continue
                   break
               break

   elif choice == 2:

       first_player =input('First player (X/O) :').upper()

       if first_player == 'X':
           print('First Player chose : X')
       elif first_player == 'O':
           print('First Player chose : O')
       else :
           print('Invalid Option')
           exit()
       if first_player == 'X':
           computer = 'O'
           print('Computer chose : O')
       else:
           computer = 'X'
           print('Computer chose : X')
    
       while True:

           try:
               first_person = int(input('Choose position (1-9): '))
           except ValueError :
               print('Invalid Position')
               continue
        
           if first_person not in range(1,10):
               print('Enter position between 1-9')
               continue
        
           if board[first_person - 1] not in ['X', 'O']:
               board[first_person - 1] = first_player
           else:
               print('Already Filled')
               continue
            
           print_board()
        
           if computer_status(first_player, computer):
               if play_again():
                   continue
               break           
        
           while True:
            
               com = random.randint(1,9)

               if board[com - 1] not in ['X', 'O']:
                   board[com - 1] = computer
                   break
           print_board()
        
           if computer_status(first_player, computer):
                if play_again():
                    continue
                break
   
   else:
       print('Enter a valid Option')
       exit()
main()
