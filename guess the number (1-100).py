import random

print('Welcome To Number Guessing Game')
game = True
while game :
    print('\nChoose Difficulty Level :')
    print('1.Easy level (1-50)')
    print('2.Medium level (1-100)')
    print('3.Hard level (1-200)')
    try:  
      choice = int(input('Enter Your Choice (1,2,3) :'))
      if choice == 1:
          limit=50
      elif choice == 2:
          limit=100
      elif choice == 3:
          limit=200
      else:
          print('\nEnter a valid choice')
          continue
      b=random.randint(1,limit)
      count = 0
      while True :
        try:  
           a = int(input(f'\n Guess the number between 1 to {limit} :'))
           print('\n',a)
           count += 1
           if a == b :
               print(f'Congratulations_You_Won in {count} attempts')
               again = input('Try Again ?(yes/no)').lower()
               if again=='yes' :
                    break
               elif again=='no':
                   print('\nThanks For Playing...')
                   game = False
                   break
               else :
                   print('Invalid Input,Closing game')
                   game=False
                   break    
           elif a>b :
                print('Too_High')
           else :
                print('Too_Low') 
        except ValueError:
             print('\nGuess_a_valid_Number')
    except ValueError:
         print('\nEnter a valid choice')