import random

toss =input('Odd Or Even :').lower()
if (toss == 'odd') or (toss == 'even'):
    computer_choice = random.randint(1,10)
else:
    print('Enter a valid option...')
    exit()
try:
    user = int(input('choose 1 to 10 :'))
except ValueError :
    print('Invalid Input')
    exit()

if user not in range(1,11):
    print('Enter a number between 1 to 10')
    exit()
print('computer chose ',computer_choice)
add = computer_choice + user
print('The total is ',add)

user_won = False
if add%2==0:
    print('Total is Even')
    if toss == 'even':
        user_won = True

else:
    print('Total is Odd')
    if toss == 'odd':
        user_won = True

def toss_deciding :
batting_second = ''      
batting_first = ''
if user_won :
    print('You Won the Toss')
    choice = input('Batting or Bowling ?:').lower()
    if choice == 'batting':
        print('You are Batting')
        print('Computer is Bowling')
        batting_first = 'user'
        batting_second = 'computer'
    elif choice == 'bowling':
        print('You are Bowling')
        print('Computer is Batting')
        batting_first = 'computer'
        batting_second = 'user'
    else:
        print('Invalid Choice')
        exit()
else:
    print('Computer Won the Toss')
    computer_decision = random.choice(['batting','bowling']).lower()
    print('Computer chose :',computer_decision)


    if computer_decision == 'batting':
        print('Computer is Batting')
        print('You are Bowling')
        batting_first = 'computer'
        batting_second = 'user'
    else:
        print('Computer is Bowling')
        print('You are Batting')
        batting_first = 'user'
        batting_second = 'computer'

            
if batting_first == 'user':
    print('\n-----FIRST INNINGS-----')
        
    score = 0
        
    while True :
        
        try:
            user_play = int(input('choose 1-10 :'))
        except ValueError :
            print('Invalid Input')
            exit()
            
        computer_play = random.randint(1,10)

        print('Computer chose',computer_play)
        if user_play not in range(1,11):
            print('Invalid run')
            continue

        if user_play == computer_play :
            print('OUT')
            break
            
        score += user_play
        print('Current Score :',score)
            
    print('Final Score :',score)
    target = score + 1
    print('Target :',target)
else:
    print('\n-----FIRST INNINGS-----')
    score = 0
        
    while True :
        
        try:
            user_play = int(input('choose 1-10 :'))
        except ValueError :
            print('Invalid Input')
            exit()
    
        computer_play = random.randint(1,10)
        print('Computer chose',computer_play)
            
        if user_play not in range(1,11):
            print('Invalid run')
            continue

        if user_play == computer_play :
            print('OUT')
            break
            
        score += computer_play
        print('Current Score :',score)
            
    print('Final Score :',score)
    target = score + 1
    print('Target :',target)

if batting_second == 'user':
    print('\n-----SECOND INNINGS-----')
        
    score = 0
        
    while True :

        try:
            user_play = int(input('choose 1-10 :'))
        except ValueError :
            print('Invalid Input')
            exit()

        computer_play = random.randint(1,10)

        print('Computer chose',computer_play)
        if user_play not in range(1,11):
            print('Invalid run')
            continue

        if user_play == computer_play :
            print('OUT')
            break
            
        score += user_play
        print('Current Score :',score)
            
        if score >= target:
            print("You Won")
            break
    if score < target:
        print('Computer Won')
else:
    print('\n-----SECOND INNINGS-----')
  
    score = 0
        
    while True :
        
        try:
            user_play = int(input('choose 1-10 :'))
        except ValueError :
            print('Invalid Input')
            exit()

        computer_play = random.randint(1,10)
        print('Computer chose',computer_play)

        if user_play not in range(1,11):
            print('Invalid run')
            continue

        if user_play == computer_play :
            print('OUT')
            break
            
        score += computer_play
        print('Current Score :',score)
            
        if score >= target:
            print('Computer Won')
            break
            
    if score < target:
            print('You Won')

